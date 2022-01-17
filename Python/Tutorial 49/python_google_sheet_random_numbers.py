# pip install gspread oauth2client
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from random import randint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("keys.json",scope)
client = gspread.authorize(creds)
sheet = client.open("Tutorial 49").sheet1
data = sheet.get_all_records()


for i in range(10):
    new_number = randint(1,100)
    sheet.append_row([new_number])