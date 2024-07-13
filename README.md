# Lambda Function For Data Pipeline Project

## Overview
This project implements the initial stage of a data pipeline that ingests data from an S3 bucket, processes it using a Lambda function, and uploads it to a Snowflake database. It includes environment configuration, modular code, and automation scripts for setup and execution.

## Contents
- **lambda_function.py**: The main Lambda function that handles data processing.
- **config.toml**: Configuration file for S3 and Snowflake details.
- **.env**: Environment variables for sensitive information (not included in the repository).
- **init.sh**: Script to initialize the environment.
- **run.sh**: Script to execute the Lambda function.
- **requirements.txt**: List of dependencies for the project.
- **.gitignore**: Specifies files and directories to be ignored by Git.

## Getting Started

### Prerequisites
- Python 3.x
- pip (Python package manager)
- AWS account with access to S3 and Snowflake
- Virtual environment (recommended)

### Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create and Activate Virtual Environment**:
   Run the `init.sh` script to set up your environment:
   ```bash
   bash init.sh
   ```

3. **Configure Environment Variables**:
   - Create a `.env` file in the project root and add your AWS and Snowflake credentials:
     ```plaintext
     AWS_A_K_ID=your_aws_access_key
     AWS_S_A_KEY=your_aws_secret_key
     SNOWFLAKE_USER=your_snowflake_user
     SNOWFLAKE_PASSWORD=your_snowflake_password
     SNOWFLAKE_ACCOUNT=your_snowflake_account
     ```

4. **Configure `config.toml`**:
   - Ensure the `config.toml` file contains the correct S3 and Snowflake configuration:
     ```toml
     [s3]
     url = "https://your-s3-bucket-url"
     bucket = "your-bucket-name"
     destination_folder = "/tmp"
     file_name = "your-file-name"
     local_file_path = "/tmp/your-file-name"

     [snowflake]
     warehouse = "your-warehouse-name"
     database = "your-database-name"
     schema = "your-schema-name"
     table = "your-table-name"
     role = "your-role-name"
     stage_name = "your-stage-name"
     ```

### Running the Project

To run the Lambda function after setting up the environment, execute the `run.sh` script:
```bash
bash run.sh
```

### Dependencies
The project requires the following Python packages. These are listed in `requirements.txt`:
- `boto3`
- `snowflake-connector-python`
- `python-dotenv`
- `toml`
- And others as specified in `requirements.txt`.

You can install them using:
```bash
pip install -r requirements.txt
```

### File Structure
```
/project-root
├── .env
├── config.toml
├── init.sh
├── lambda_function.py
├── requirements.txt
├── run.sh
└── .gitignore
```

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
- [AWS](https://aws.amazon.com/)
- [Snowflake](https://www.snowflake.com/)
- [Python](https://www.python.org/)
