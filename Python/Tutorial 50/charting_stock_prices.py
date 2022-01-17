# pip install gspread oauth2client matplotlib
import requests
from bs4 import BeautifulSoup
from time import sleep
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt
def stock_price():
    url = "https://finance.yahoo.com/quote/YM=F/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    price = soup.find("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
    return price

price = stock_price()
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("keys.json",scope)
while True:
    new_price = stock_price()
    if new_price != price:
        price = new_price
        client = gspread.authorize(creds)
        sheet = client.open("Tutorial 50").sheet1
        data = sheet.get_all_records()
        sheet.append_row([price])
        y = sheet.col_values(1)
        for i in range(0,len(y)):
            y[i] = float(y[i].replace(",",""))
        plt.plot(y)
        plt.title("Dow Futures")
        plt.ylabel("Values")
        plt.show()
    sleep(1)