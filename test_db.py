from config import get_connection
def test_connection():
    try:
        conn = get_connection()
        print("✅ Database connection successful!")
        conn.close()
    except Exception as e:
        print("❌ Failed to connect to the database:")
        print(e)


# if __name__ == "__main__":
#     test_connection()