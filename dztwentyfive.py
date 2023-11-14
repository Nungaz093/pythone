from random import choice
import json


def gen_person():
    key = ''
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(key) != 8:
        key += choice(nums)

    while len(name) != 7:
        name += choice(letters)
    # print(name)

    while len(tel) != 10:
        tel += choice(nums)
    # print(tel)

    person = {key: {
        'name': name,
        'tel': tel
    }}

    return person


def write_json(person_dict):
    try:
        data = json.load(open("persons_json"))
    except FileNotFoundError:
        data = []
    data.append(person_dict)
    with open('persons_json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())