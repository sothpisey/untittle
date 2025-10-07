import mysql.connector
from mysql.connector import Error
from .config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except Error as e:
        print(f"Database connection error: {e}")
        return None
