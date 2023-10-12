f = open('zadacha.txt', 'w', encoding="UTF-8")
f.write("Замена строки в текстовом файле\nизменить строку в списке\nзапись списков в файле\n")
f.close()

f = open("zadacha.txt", "r", encoding="UTF-8")
read_file = f.readlines()
print(read_file)
f.close()

f = open('zadacha.txt', 'w', encoding="UTF-8")
try:
    int_put = int(input("№1: ")) - 1
    int_puts = int(input("№2: ")) - 1
    if 0 <= int_put <= len(read_file) or 0 <= int_puts <= len(read_file):
        read_file[int_put], read_file[int_puts] = read_file[int_puts], read_file[int_put]
# elif 0 <= int_puts <= len(read_file):
#     read_file[int_put], read_file[int_puts] = read_file[int_puts], read_file[int_put]
    else:
        print("Индекс введен не верно!")

    f.writelines(read_file)
    print(read_file)
    f.close()
except IndexError:
    print("Ошибка нет такой строки!!!")
