import os
import psycopg2  
import pandas as pd
from datetime import datetime

# Settings
DB_CONFIG = {
    'postgres_db': 'northwind',
    'postgres_user': 'northwind_user',
    'postgres_password': 'thewindisblowing',
    'host': 'localhost',
    'port': 5432
}

OUTPUT_DIR = '/data/postgres'

# Function to extract data and save to CSV
def extract_and_save_table(table_name, output_dir):
    conn = psycopg2.connect(**DB_CONFIG)
    query = f'SELECT * FROM {table_name}'
    df = pd.read_sql_query(query, conn)
    date_str = datetime.now().strftime('%Y-%m-%d')
    output_path = os.path.join(output_dir, table_name, date_str)
    os.makedirs(output_path, exist_ok=True)
    file_path = os.path.join(output_path, f'{table_name}.csv')
    df.to_csv(file_path, index=False)
    conn.close()

# List tables and extract data
tables = ['orders', 'customers', 'products'] 
for table in tables:
    extract_and_save_table(table, OUTPUT_DIR)
