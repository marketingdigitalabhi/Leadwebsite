from flask import Flask, jsonify, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Google Sheets Setup
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", SCOPE)
client = gspread.authorize(CREDS)

# Replace with your Google Sheet ID
SHEET_ID = "YOUR_SHEET_ID"
sheet = client.open_by_key(SHEET_ID).sheet1

@app.route("/api/data")
def get_data():
    records = sheet.get_all_records()  # Returns list of dicts
    return jsonify(records)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
