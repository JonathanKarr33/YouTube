# pip install gspread oauth2client
import gspread
from oauth2client import client
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("keys.json",scope)
client = gspread.authorize(creds)
sheet = client.open("Tutorial 49").sheet1
data  = sheet.get_all_records()

row = sheet.row_values(1)
col = sheet.col_values(2)
cell = sheet.cell(1,2).value
num_rows = sheet.row_count
print(num_rows)
sheet.update_cell(2,2,"Updated Value")
sheet.append_row([2,5,"A"])