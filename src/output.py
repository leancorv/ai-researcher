import os
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_sheet():
    creds = Credentials.from_service_account_file(
        "google-credentials.json",
        scopes=SCOPES
    )
    client = gspread.authorize(creds)
    sheet = client.open_by_key(os.getenv("GOOGLE_SHEET_ID"))
    return sheet.sheet1

def save_result(result: dict):
    """
    Guarda el resultado del agente en Google Sheets.
    """
    sheet = get_sheet()

    # Si la hoja está vacía, agregamos headers
    if sheet.row_count == 0 or sheet.cell(1, 1).value is None:
        sheet.append_row([
            "Fecha", "Tema", "Query usado",
            "Score", "Estado", "Razón", "Resumen"
        ])

    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M"),
        result.get("topic", ""),
        result.get("query_used", ""),
        result.get("score", ""),
        result.get("status", ""),
        result.get("reason", ""),
        result.get("summary", "") or "—"
    ]

    sheet.append_row(row)
    print(f"💾 Guardado en Google Sheets (score: {result.get('score')}/10)")