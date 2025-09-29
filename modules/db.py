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

def update_expense(expense_id, date=None, category=None, description=None, amount=None):
    """
    Update only the provided fields of the expense with id = expense_id.
    Pass None for any field you don't want to change.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        updates = []
        params = []

        if date is not None:
            updates.append("date = %s")
            params.append(date)
        if category is not None:
            updates.append("category = %s")
            params.append(category)
        if description is not None:
            updates.append("description = %s")
            params.append(description)
        if amount is not None:
            updates.append("amount = %s")
            params.append(amount)

        if not updates:
            print("❌ No fields provided to update.")
            return

        params.append(expense_id)
        sql = f"UPDATE expenses SET {', '.join(updates)} WHERE id = %s"
        cur.execute(sql, tuple(params))

        if cur.rowcount == 0:
            print(f"⚠️  No expense found with id = {expense_id}.")
        else:
            conn.commit()
            print(f"✅ Expense {expense_id} updated successfully.")

    except Exception as e:
        conn.rollback()
        print("❌ Failed to update expense:", e)
        raise
    finally:
        cur.close()
        conn.close()


def delete_expense(expense_id):
    """
    Delete the expense row with the given id.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
        if cur.rowcount == 0:
            print(f"⚠️  No expense found with id = {expense_id}. Nothing deleted.")
        else:
            conn.commit()
            print(f"🗑️  Expense {expense_id} deleted successfully.")
    except Exception as e:
        conn.rollback()
        print("❌ Failed to delete expense:", e)
        raise
    finally:
        cur.close()
        conn.close()

