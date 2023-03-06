import send_mail
import requests
from bs4 import BeautifulSoup
import strings

response = requests.get(url = strings.url, headers= strings.header)

html = response.text

tomato = BeautifulSoup(html, "lxml")

price = tomato.select_one(selector="div.aok-align-center span.a-offscreen")
price_actual = int(price.getText()[1:].replace(",",""))

price_budget =  int(input("Please enter your budget in INR: "))

if price_actual <= price_budget:
    send_mail.send_mail(price_actual, strings.url)