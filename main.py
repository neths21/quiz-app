import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()
# Configuration
file_path =r'D:\code\python\quizapp\data\bix_ca.csv'  # Replace with your CSV file path
db_config = {
    'host': 'localhost',
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': 'quiz_db'
}
table = 'test'

# Load CSV
df = pd.read_csv(file_path)

# Connect to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Insert data
insert_query = f"INSERT INTO {table} ({', '.join(df.columns)}) VALUES ({', '.join(['%s'] * len(df.columns))})"
cursor.executemany(insert_query, df.values.tolist())
conn.commit()

print(f"Created table '{table}' and imported {cursor.rowcount} rows.")
cursor.close()
conn.close()
