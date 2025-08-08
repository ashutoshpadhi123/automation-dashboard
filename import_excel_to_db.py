import pandas as pd
import sqlite3

# Load Excel file
excel_file = "AutomationData.xlsx"

# Read each sheet
df_ui = pd.read_excel(excel_file, sheet_name="UI Automation")
df_api = pd.read_excel(excel_file, sheet_name="API Automation")

# Save to SQLite
conn = sqlite3.connect("data.db")

df_ui.to_sql("ui_automation", conn, if_exists="replace", index=False)
df_api.to_sql("api_automation", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully from Excel!")