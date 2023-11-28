import requests
from bs4 import BeautifulSoup
import csv


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")
        news = self.html.find_all("div", class_="product-card oneclick-enabled")
        for item in news:
            title = item.find("div", class_="product-card__name").text.strip()
            rub = item.find("span", class_="price-new").text
            htmlz = item.find("a")["href"]
            self.res.append({
                'title': title,
                'rub': rub,
                'htmlz': htmlz
            })
            # print(self.res)

    def write_save(self):
        with open(self.path, "w") as f:
            a = 1
            for item in self.res:
                f.write(f"Покупка №{a}\nНазвание:{item['title']}\nЦена:{item['rub']}\nСсылка:{item['htmlz']}\n\n\n")
                a += 1

    def info(self):
        self.get_html()
        self.write_save()
