"""
Ingest CSV files into SQLite database using pandas and sqlite3.
Replaces tables if they already exist.
"""

import pandas as pd
import sqlite3
import os

def ingest_csv_to_sqlite():
    """Load CSV files into SQLite database"""
    print("Loading data into SQLite database...")
    
    # Database name
    db_name = 'ecom.db'
    
    # Remove existing database if it exists
    if os.path.exists(db_name):
        os.remove(db_name)
        print(f"Removed existing database: {db_name}")
    
    # Create connection to SQLite database
    conn = sqlite3.connect(db_name)
    
    # CSV files and their table names
    csv_files = {
        'customers.csv': 'customers',
        'products.csv': 'products',
        'orders.csv': 'orders',
        'order_items.csv': 'order_items',
        'payments.csv': 'payments'
    }
    
    # Read and load each CSV file
    for csv_file, table_name in csv_files.items():
        if os.path.exists(csv_file):
            # Read CSV file
            df = pd.read_csv(csv_file)
            
            # Write to SQLite database (replace if exists)
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            print(f"Loaded {len(df)} rows from {csv_file} into table '{table_name}'")
        else:
            print(f"Warning: {csv_file} not found. Skipping...")
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print("✅ Data loaded into SQLite successfully")

if __name__ == "__main__":
    ingest_csv_to_sqlite()

