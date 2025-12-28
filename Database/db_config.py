import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            port=int(os.getenv("MYSQL_PORT")),
            database=os.getenv("MYSQL_DB"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            connection_timeout=3
        )
        print("✅ Database connection SUCCESS")
        return connection

    except mysql.connector.Error as err:
        print("❌ Database connection FAILED")
        print(f"MySQL Error: {err}")
        return None
