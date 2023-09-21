try:
    x = {
        'John': {
            'N': 3056,
            'S': 8463,
            'E': 8441,
            'W': 2694
        },
        'Tom': {
            'N': 4832,
            'S': 6786,
            'E': 4737,
            'W': 3612
        },
        'Anne': {
            'N': 5239,
            'S': 4802,
            'E': 5820,
            'W': 1859
        },
        'Fiona': {
            'N': 3904,
            'S': 3645,
            'E': 8821,
            'W': 2451
        }
    }
    for i in x:
        print(i)
        for j in x[i]:
            print(f'{j} : {x[i][j]}')
        print("Выберите имя (John,Tom,Anne,Fiona)")
        name = input("name: ")
        print("Выберите регион: ")
        region = input("region(N,S,E,W): ")
        print(x[name][region])
        print("Введите объем продаж: ")
        x[name][region] = int(input())
        print(x[name])
except KeyError:
    print("Нет такого имени и региона!!")
