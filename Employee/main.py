from Employee import AdmWorker, Worker, Trader

lst = (AdmWorker.AdmWorker('Валерий', 'Задорожный', 1, 400),
       Worker.Worker('Илья', 'Кромин', 2, 5),
       Trader.Trader('Николай', 'Хорольский', 3, 800, 10000))

print('Расчет заработной платы\n'
      f'{"+" * 40}')
for i in lst:
    i.info()
    print()