import pandas as pd
import matplotlib.pyplot as plt

def plot_category_spend(df):
    df = df.copy()
    # print(df.dtypes)  - amount was object i was getting error
    # Ensure 'amount' is numeric
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df.dropna(subset=["amount"], inplace=True)

    category_summary = df.groupby("category")["amount"].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    category_summary.plot(kind="bar")
    plt.title("Category-wise Spending")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.tight_layout()
    plt.savefig("CategorywiseSpend.png")
    plt.show()

def plot_monthly_spend(df):
    df = df.copy()

    # Ensure 'amount' is numeric
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df.dropna(subset=["amount"], inplace=True)

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M").astype(str)
    monthly_summary = df.groupby("month")["amount"].sum()
    plt.figure(figsize=(8, 5))
    monthly_summary.plot(kind="line", marker='o')
    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Amount")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Monthly_Spend.png")
    plt.show()

def plot_category_pie(df):
    df = df.copy()
    
    # Ensure 'amount' is numeric
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df.dropna(subset=["amount"], inplace=True)
    
    # Group by category and take top 6
    category_summary = df.groupby("category")["amount"].sum().sort_values(ascending=False).head(6)
    
    # Create pie chart without percentage labels inside
    plt.figure(figsize=(8, 6))
    wedges, _ = plt.pie(
        category_summary,
        startangle=140,
        wedgeprops={'linewidth': 1, 'edgecolor': 'white'}
    )
    
    # Add legend (outside the plot)
    plt.legend(
        wedges,
        category_summary.index,
        title="Categories",
        loc="center left",
        bbox_to_anchor=(1, 0.5),
        fontsize=10
    )
    
    plt.title("Spending by Category (Pie Chart)")
    plt.tight_layout()
    plt.savefig("category_pie_chart.png")
    plt.show()


def plot_amount_histogram(df):
    df = df.copy()
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df.dropna(subset=["amount"], inplace=True)

    plt.figure(figsize=(7, 5))
    plt.hist(df["amount"], bins=10, edgecolor="black")
    plt.title("Spending Distribution (Histogram)")
    plt.xlabel("Amount")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("amount_histogram.png")
    plt.show()
