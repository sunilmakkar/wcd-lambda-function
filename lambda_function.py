import os
import boto3
import requests
import snowflake.connector as sf
from dotenv import load_dotenv
import toml

# Load environment variables from .env
load_dotenv()

# Load configuration from config.toml
with open('config.toml', 'r') as f:
    config = toml.load(f)

def download_file_from_s3(bucket_name, file_name, local_file_path):
    """Download a file from S3."""
    client = boto3.client('s3',
                           aws_access_key_id=os.getenv('AWS_A_K_ID'),
                           aws_secret_access_key=os.getenv('AWS_S_A_KEY'))
    client.download_file(Bucket=bucket_name, Key=file_name, Filename=local_file_path, ExtraArgs={'RequestPayer': 'requester'})

def create_snowflake_connection():
    """Create a connection to Snowflake."""
    return sf.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse=config['snowflake']['warehouse'],
        database=config['snowflake']['database'],
        schema=config['snowflake']['schema'],
        role=config['snowflake']['role']
    )

def upload_file_to_snowflake(cursor, local_file_path, stage_name):
    """Upload a local file to Snowflake stage."""
    cursor.execute(f"CREATE OR REPLACE FILE FORMAT COMMA_CSV TYPE ='CSV' FIELD_DELIMITER = ',';")
    cursor.execute(f"CREATE OR REPLACE STAGE {stage_name} FILE_FORMAT = COMMA_CSV")
    cursor.execute(f"PUT 'file://{local_file_path}' @{stage_name}")
    cursor.execute(f"LIST @{stage_name}")

def load_data_into_table(cursor, schema, table, stage_name, file_name):
    """Load data from stage into Snowflake table."""
    cursor.execute(f"TRUNCATE TABLE {schema}.{table};")
    cursor.execute(f"COPY INTO {schema}.{table} FROM @{stage_name}/{file_name} ON_ERROR='CONTINUE' FILE_FORMAT = COMMA_CSV;")

def lambda_handler(event, context):
    """Main Lambda function handler."""
    url = config['s3']['url']
    destination_folder = '/tmp'
    file_name = 'inventory.csv'
    local_file_path = os.path.join(destination_folder, file_name)
    
    # Download file
    download_file_from_s3(config['s3']['bucket'], file_name, local_file_path)

    # Establish Snowflake connection
    conn = create_snowflake_connection()
    cursor = conn.cursor()

    # Upload and load data
    upload_file_to_snowflake(cursor, local_file_path, config['snowflake']['stage_name'])
    load_data_into_table(cursor, config['snowflake']['schema'], config['snowflake']['table'], config['snowflake']['stage_name'], file_name)

    print("File uploaded to Snowflake successfully.")

    return {
        'statusCode': 200,
        'body': 'File downloaded and uploaded to Snowflake successfully.'
    }
