import re


def wall_pass(pacc):
    return re.findall(r'^[a-z0-9@_-]{6,18}$', pacc)


print(wall_pass(input("Введите пароль: ")))

# numz = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78'
#
# reg = r'\+?7\s?\(?\d{3}\)?\s?\d{3}[\s-]?\d{2}[\s-]?\d{2}'
#
# print(re.findall(reg, numz))
