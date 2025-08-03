from analytics import load_data, monthly_summary,top_categories

def test_analytics_functions():
    df = load_data()
    print("\n✅ Loaded Data:")
    print(df)

    summary = monthly_summary(df)
    print("\n📊 Monthly Summary:")
    print(summary)

    topExpense_categories =top_categories(df)
    print("\n📊 top categories:")
    print(topExpense_categories)

if __name__ == "__main__":
    test_analytics_functions()
