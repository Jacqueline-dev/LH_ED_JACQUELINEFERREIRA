import os
import pandas as pd
from sqlalchemy import create_engine

DB_CONFIG = {
    'postgres_db': 'northwind',
    'postgres_user': 'northwind_user',
    'postgres_password': 'thewindisblowing',
    'host': 'localhost',
    'port': 5432
}

engine = create_engine(f'postgresql://{DB_CONFIG["user"]}:{DB_CONFIG["password"]}@{DB_CONFIG["host"]}:{DB_CONFIG["port"]}/{DB_CONFIG["dbname"]}')

def load_data_to_db(file_path, table_name):
    df = pd.read_csv(file_path)
    df.to_sql(table_name, engine, if_exists='replace', index=False)

# Paths to extracted data
postgres_data_path = '/data/postgres'
csv_data_path = '/data/csv'

# Load PostgreSQL data
for root, dirs, files in os.walk(postgres_data_path):
    for file in files:
        if file.endswith('.csv'):
            table_name = os.path.basename(root)
            file_path = os.path.join(root, file)
            load_data_to_db(file_path, table_name)

# Upload CSV data
for root, dirs, files in os.walk(csv_data_path):
    for file in files:
        if file == 'order_details.csv':
            file_path = os.path.join(root, file)
            load_data_to_db(file_path, 'order_details')
