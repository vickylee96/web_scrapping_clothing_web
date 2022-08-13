
from email import header
import requests
from bs4 import BeautifulSoup
from csv import writer

req = requests.get("https://cottonon.com/ZA/factorie/f-sale/f-sale-womens/")
soup = BeautifulSoup(req.text,'html.parser')
results = soup.find_all('div',{'class':'product-tile'})


# with open('price list.csv','w',encoding='utf8',newline='') as f:
#     thewriter = writer(f)
#     header = ["product name, prices"]
#     thewriter.writerow(header)

for item in results:
    products = item.find('div',{'class':'product-name'}).text.replace('\n',"")
    price = item.find('span',{'class':'product-sales-price'}).text.replace('\n',"")
     
        # details = [products,price]
        # thewriter.writerow(details)
    print(products,float(price))