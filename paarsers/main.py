from parser import Parser


def main():
    for i in range(1, 4):
        pars = Parser("https://glavsnab.net/otdelochnie-materiali/lakokrasochnye-materialy/koleri-i-toneri.html",
                      "katalog.txt")
        pars.info()


if __name__ == '__main__':
    main()

# r = requests.get("https://pazavto.ru")
# print(r.status_code)
