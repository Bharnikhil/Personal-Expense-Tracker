import argparse
from db import add_expense, fetch_all_expenses, create_table
from analytics import load_data  # Or your DB fetch
from visuals import plot_category_spend, plot_monthly_spend,plot_category_pie, plot_amount_histogram
from analytics import run_export


def main():
    parser=argparse.ArgumentParser(description="📊 Personal Expense Tracker")
    subparsers=parser.add_subparsers(dest="command")

    #subcommand: add
    add_parser=subparsers.add_parser("add",help="Add a new expense!")
    add_parser.add_argument("date",type=str, help="Date (YYYY-MM-DD)")
    add_parser.add_argument("category",type=str, help="Expense category")
    add_parser.add_argument("description",type=str, default="", help="Optional description")
    add_parser.add_argument("amount",type=float, help="Amount spent")

    # Subcommand: view
    view_parser = subparsers.add_parser("view", help="View all expenses")
    view_parser.add_argument("--category", help="Filter by category")
    view_parser.add_argument("--month", help="Filter by month (format: YYYY-MM)")

    # Inside your argparse setup  - export subcommand
    export_parser = subparsers.add_parser("export", help="Export expenses to CSV or HTML")
    export_parser.add_argument("--filetype", choices=["csv", "html"], required=True)
    export_parser.add_argument("--filename", type=str, default="report")

    #parser for visulaization part
    visual_parser = subparsers.add_parser("visual", help="Visualize expense data")
    visual_parser.add_argument(
        "--type", 
        choices=["category", "monthly", "pie", "histogram"], 
        required=True, 
        help="Type of visualization (category, monthly, pie, histogram)"
    )



    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.date, args.category, args.description, args.amount)
        print("✅ Expense added successfully.")

    elif args.command == "view":
        expenses = fetch_all_expenses()
        category_filter = args.category
        month_filter = args.month
        filtered = []

        for exp in expenses:
            date_str = str(exp[1])  # Convert date to string like '2025-06-15'
            match_category = category_filter is None or exp[2].lower() == category_filter.lower()
            match_month = month_filter is None or date_str.startswith(month_filter)

            if match_category and match_month:
                filtered.append(exp)

        if not filtered:
            print("❌ No matching expenses found.")
        else:
            print("📄 Filtered Expenses:")
            for exp in filtered:
                print(f"{exp[0]} | {exp[1]} | ₹{exp[4]} | {exp[2]} | {exp[3]}")

    elif args.command == "export":
        df = load_data()
        run_export(df, args.filetype, args.filename)

    elif args.command == "visual":
        df = load_data()
        if args.type == "category":
            plot_category_spend(df)
        elif args.type == "monthly":
            plot_monthly_spend(df)
        elif args.type == "pie":
            plot_category_pie(df)
        elif args.type == "histogram":
            plot_amount_histogram(df)


    else:
        parser.print_help()

if __name__ == "__main__":
    create_table()  # Ensure table exists before anything
    main()



