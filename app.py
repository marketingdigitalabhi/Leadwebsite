import os, json
from flask import Flask, jsonify, render_template
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Google Sheets Setup
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from environment variable
creds_json = os.getenv("GOOGLE_CREDENTIALS")
if not creds_json:
    raise Exception("GOOGLE_CREDENTIALS environment variable not set!")

creds_dict = json.loads(creds_json)
creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPE)
client = gspread.authorize(creds)

# Replace with your Google Sheet ID
SHEET_ID = "1CswGuv2YzM0ezHvnA6vakwyjyZTdsSoiWMlUX7oPfMU"
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
