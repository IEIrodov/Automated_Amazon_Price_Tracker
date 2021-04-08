import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "Your Email Id"
MY_PASSWORD = "Your Email Id Password"
PRICE = 90.00
URL = "https://www.amazon.com/dp/B00FLYWNYQ/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B00FLYWNYQ&pd_rd_w=Ndgz5&pf_rd_p=cbc856ed-1371-4f23-b89d-d3fb30edf66d&pd_rd_wg=3Rsms&pf_rd_r=6VWT256C6GHSV5B6RHWT&pd_rd_r=cd570051-aaec-48fa-a09f-0291e8a858da&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTDVXODJONEpWU1UzJmVuY3J5cHRlZElkPUEwMzk3MzMwMVBUMTQzSVZFTjNGVCZlbmNyeXB0ZWRBZElkPUEwMDYwNTYyMzBEUVRUU1NHNllQViZ3aWRnZXROYW1lPXNwX2RldGFpbF90aGVtYXRpYyZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Accept_Language":"en-US,en;q=0.9"
}

response = requests.get(URL,headers=headers)

website_html = response.text

soup = BeautifulSoup(website_html,"lxml")

#print(soup.prettify())

price = soup.find("span",id="priceblock_ourprice").getText()
title = soup.find(id="productTitle").getText().strip()

current_price = float(price.split("$")[1])

if current_price<=PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"PYTHON BOT[PRICE DROP ALERT]\n\n The {title.encode('utf8')}\n Price is ${current_price},below your target price.Buy now!\n{URL}"
        )

