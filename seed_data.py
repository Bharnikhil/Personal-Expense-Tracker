# for storing the data in bulk through cli 
# if you are an household wife you dont have bulk data you can do this manually one by one 
# for experimentation purpose i wanted an automated way to send this data in bulk to my database so 
#a separate script like seed_data.py that runs once and inserts all sample records into the database

from config  import get_connection  # Make sure this function is working correctly

def insert_sample_expenses():
    data = [
        ("2025-03-05", "Shopping", "New jeans", 1800),
        ("2025-03-15", "Food", "Dinner at cafe", 900),
        ("2025-04-12", "Assets", "Bought gaming console", 30000),
        ("2025-04-25", "Entertainment", "Concert ticket", 2200),
        ("2025-05-09", "Food", "Birthday cake", 600),
        ("2025-05-22", "Shopping", "T-shirt for trip", 850),
        ("2025-06-03", "Gifts", "Anniversary watch", 5500),
        ("2025-06-28", "Transport", "Cab fares", 1300),
        ("2025-08-07", "Electronics", "Bluetooth speaker", 3000),
        ("2025-08-16", "Assets", "Laptop upgrade", 85000),
        ("2025-09-01", "Entertainment", "Online course subscription", 1200),
        ("2025-09-21", "Food", "Midnight snacks", 300),
    ]

    conn = get_connection()
    cur = conn.cursor()
    cur.executemany("""
        INSERT INTO expenses (date, category, description, amount)
        VALUES (%s, %s, %s, %s);
    """, data)
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Sample data inserted.")

# if __name__ == "__main__":
#     insert_sample_expenses()