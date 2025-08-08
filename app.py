import os
from flask import Flask, jsonify, send_from_directory
import sqlite3

if os.environ.get("IMPORT_ON_START", "false").lower() == "true":
    import import_excel_to_db
    print("Excel imported into SQLite before server start.")

app = Flask(__name__, static_folder="static")

def get_data(table_name):
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    rows = conn.execute(f"SELECT * FROM {table_name}").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.route("/api/data")
def api_data():
    return jsonify({
        "ui_automation": get_data("ui_automation"),
        "api_automation": get_data("api_automation")
    })

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)