# export.py
def export_to_csv(df, filename="report.csv"):
    df.to_csv(filename, index=False)
    print(f"✅ Exported to {filename}")

def export_to_html(df, filename="report.html"):
    df.to_html(filename, index=False)
    print(f"✅ Exported to {filename}")
