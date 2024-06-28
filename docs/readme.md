# Data Pipeline Project

## Overview

This project implements a data pipeline using PostgreSQL, Apache Airflow, and Meltano. The pipeline extracts data from a PostgreSQL database and a CSV file, processes it, and loads it into a final PostgreSQL database.

## Prerequisites

- PostgreSQL
- Python
- Apache Airflow
- Meltano

## Setup

1. **PostgreSQL Configuration:**
   - Install PostgreSQL and create the necessary databases.

2. **Airflow Configuration:**
   - Install Airflow:
     ```sh
     pip install apache-airflow
     airflow db init
     airflow users create --username admin --password admin --firstname First --lastname Last --role Admin --email admin@example.com
     ```
   - Place the `data_pipeline_dag.py` file in the `dags/` directory.

3. **Meltano Configuration:**
   - Install Meltano:
     ```sh
     pip install meltano
     meltano init my_project
     cd my_project
     meltano add extractor tap-postgres
     meltano add loader target-postgres
     ```
   - Update the `meltano.yml` file with the provided configuration.

4. **Scripts:**
   - Place the scripts (`extract_postgres.py`, `process_csv.py`, `load_data.py`) in the `scripts/` directory.

5. **Data:**
   - Ensure the CSV file is placed in the correct directory.

## Running the Pipeline

1. Start the Airflow webserver and scheduler:
   ```sh
   airflow webserver
   airflow scheduler