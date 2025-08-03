import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "database": "expense_db",
    "user": "postgres",
    "password": "S19T20V22K11"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)    