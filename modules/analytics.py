import pandas as pd
from modules.db import fetch_all_expenses
from modules.export import export_to_csv, export_to_html
import matplotlib.pyplot as plt

from modules.visuals import (
    plot_category_spend,
    plot_monthly_spend,
    plot_category_pie,
    plot_amount_histogram
)



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

def top_categories(df,n):
    """
    Returns the top N categories by total spend.
    """
    return df.groupby('category')['amount'].sum().sort_values(ascending=False).head(n)

def summary_report(df):
    """
    Prints an overall summary of expenses:
    - Total number of expenses
    - Total spend
    - Average spend per expense
    """
    total_spend = df['amount'].sum()
    total_expenses = len(df)
    avg_spend = df['amount'].mean()

    print("\n📊 Overall Summary:")
    print(f"Total Expenses: {total_expenses}")
    print(f"Total Spend: ₹{total_spend:.2f}")
    print(f"Average Spend per Expense: ₹{avg_spend:.2f}")




def run_export(df, filetype='csv', filename='report'):
    if filetype == 'csv':
        export_to_csv(df, f"{filename}.csv")
    elif filetype == 'html':
        export_to_html(df, f"{filename}.html")
    else:
        print("❌ Unsupported export type. Choose csv or html.")






# Test if run directly  - temporary test block
# if __name__ == "__main__":
#     df = load_data()
#     print("📅 Monthly Summary:")
#     print(monthly_summary(df))
    
#     print("\n🔥 Top Spending Categories:")
#     print(top_categories(df))





    
