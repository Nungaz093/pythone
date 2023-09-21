mathick = {'Matvei', 'Evgenia', 'Michail', 'Maxim', 'Natalia'}
fizisk = {'Maxim', 'Matvei', 'Alexandr'}
all_priz = mathick | fizisk
print("Все призеры: ", all_priz)

twoolimp = mathick & fizisk
print("Призы обеих команд: ", twoolimp)

new_list = mathick & fizisk
print("Обновленный список призеров по математике: ", new_list)