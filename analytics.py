import pandas as pd
from db import fetch_all_expenses

def load_data():
    """
    Loads all expenses from the database into a Pandas DataFrame.
    """
    records = fetch_all_expenses()
    df = pd.DataFrame(records, columns=["id", "date", "category", "description", "amount"])
    df['date'] = pd.to_datetime(df['date'])  # Ensure 'date' is datetime
    return df

def monthly_summary(df):
    """
    Groups expenses by month and category, returning a summary table.
    """
    df['month'] = df['date'].dt.to_period('M')
    summary = df.groupby(['month', 'category'])['amount'].sum().unstack().fillna(0)
    return summary

def top_categories(df, n=5):
    """
    Returns the top N categories by total spend.
    """
    return df.groupby('category')['amount'].sum().sort_values(ascending=False).head(n)

# Test if run directly  - temporary test block
if __name__ == "__main__":
    df = load_data()
    print("📅 Monthly Summary:")
    print(monthly_summary(df))
    
    print("\n🔥 Top Spending Categories:")
    print(top_categories(df))



    
