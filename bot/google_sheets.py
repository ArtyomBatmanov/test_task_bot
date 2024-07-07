import gspread
from oauth2client.service_account import ServiceAccountCredentials
from .config import GOOGLE_SHEETS_CREDENTIALS_FILE, SHEET_NAME


def connect_to_google_sheets():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        GOOGLE_SHEETS_CREDENTIALS_FILE, scope
    )
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).sheet1
    return sheet


def get_google_sheet_value(cell):
    sheet = connect_to_google_sheets()
    value = sheet.acell(cell).value
    return value


def append_date_to_sheet(date):
    sheet = connect_to_google_sheets()
    sheet.append_row([date], table_range="B1")
