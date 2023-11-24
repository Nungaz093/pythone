import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_cvs(data):
    with open('parsdz.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\r', delimiter=";")
        writer.writerow((data['name'], data['kol'], data['brend']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    s = soup.find("div", class_="c-list__list")
    plugin = s.find_all("div", class_="c-list__item card")
    for plu in plugin:
        name = plu.find("span", class_="card__title").text.strip()
        kol = plu.find("p", class_="card__amount").text
        brend = plu.find("a", class_="card__country").text

        data = {
            'name': name,
            'kol': kol,
            'brend': brend,
        }
        write_cvs(data)


def main():
    url = "https://ural.toys/catalog/359/"
    get_data(get_html(url))


if __name__ == '__main__':
    main()

# r = requests.get("https://refo24.ru")
# print(r.status_code)
