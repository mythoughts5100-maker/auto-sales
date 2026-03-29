import os
import psycopg2
import random
from datetime import datetime

DB_URL = os.environ.get("DB_URL")

def insert_row():
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id SERIAL PRIMARY KEY,
            sale_date DATE,
            product VARCHAR(50),
            region VARCHAR(50),
            sales_amount INT
        );
    """)

    for _ in range(5):
        cursor.execute("""
            INSERT INTO sales (sale_date, product, region, sales_amount)
            VALUES (%s, %s, %s, %s)
        """, (
            datetime.now().date(),
            random.choice(["Laptop", "Phone", "Tablet"]),
            random.choice(["Baku", "Ganja", "Sumqayit"]),
            random.randint(100, 1000)
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print("Inserted 5 rows")

if __name__ == "__main__":
    insert_row()