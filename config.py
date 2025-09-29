import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "database": "expense_db",
    "user": "postgres",
    "password": "Your Password here"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)    