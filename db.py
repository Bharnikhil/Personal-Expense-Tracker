# db.py

from config import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            category VARCHAR(50),
            description TEXT,
            amount NUMERIC(10, 2)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def add_expense(date, category, description, amount):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO expenses (date, category, description, amount)
        VALUES (%s, %s, %s, %s);
    """, (date, category, description, amount))
    conn.commit()
    cur.close()
    conn.close()

def fetch_all_expenses():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses ORDER BY date DESC;")
    rows = cur.fetchall()  # datatype of rows will be list of tuple of records 
    """
    like this!!
    [
    (1, '2025-07-30', 'food', 'Veggies', 120),
    (2, '2025-07-29', 'travel', 'Metro recharge', 60)
]

    """
    cur.close()
    conn.close()
    return rows
