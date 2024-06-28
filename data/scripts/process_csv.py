import os
import pandas as pd
from datetime import datetime

CSV_FILE = '/path/to/order_details.csv'
OUTPUT_DIR = '/data/csv'

# Process and save CSV
def process_csv(file_path, output_dir):
    df = pd.read_csv(file_path)
    date_str = datetime.now().strftime('%Y-%m-%d')
    output_path = os.path.join(output_dir, date_str)
    os.makedirs(output_path, exist_ok=True)
    file_path = os.path.join(output_path, 'order_details.csv')
    df.to_csv(file_path, index=False)

process_csv(CSV_FILE, OUTPUT_DIR)

