import os, json
from flask import Flask, jsonify, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Google Sheets Setup
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials from environment
creds_json = os.getenv("GOOGLE_CREDENTIALS")
if not creds_json:
    raise Exception("GOOGLE_CREDENTIALS environment variable not set!")

creds_dict = json.loads(creds_json)
CREDS = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, SCOPE)
client = gspread.authorize(CREDS)

# Replace with your Google Sheet ID
SHEET_ID = "YOUR_SHEET_ID"
sheet = client.open_by_key(SHEET_ID).sheet1

@app.route("/api/data")
def get_data():
    records = sheet.get_all_records()
    return jsonify(records)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
