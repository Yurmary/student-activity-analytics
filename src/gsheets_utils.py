import gspread
from google.oauth2.service_account import Credentials

def update_google_sheets(aggregated_data):
    creds = Credentials.from_service_account_file(
        "/content/earnest-entry-455201-j6-6d301227605d.json",
        scopes=["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    )
    gc = gspread.authorize(creds)

    spreadsheet = gc.create("Aggregated Data")
    worksheet = spreadsheet.get_worksheet(0)

    data_to_upload = aggregated_data.columns.tolist() + aggregated_data.values.tolist()
    worksheet.update(range_name="A1", values=data_to_upload)
