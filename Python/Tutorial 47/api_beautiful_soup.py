import requests
from bs4 import BeautifulSoup
from time import sleep
def stock_price():
    url = "https://finance.yahoo.com/quote/%5EIXIC?p=^IXIC&.tsrc=fin-srch"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    price = soup.find("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
    return price

price = stock_price()
print("\n The Nasdaq is: "+ str(price),end ="")
while True:
    new_price = stock_price()
    if new_price != price:
        price = stock_price()
        print("\r The Nasdaq is: "+ str(price),end="")
    sleep(1)