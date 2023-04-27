while True:
    grats_temp = input('Введите шаблон поздравления,'
                       'в шаблоне нужно использовать конструкцию'
                        '{name} и {age}: ')
    if '{name}' in grats_temp and '{age}' in grats_temp:
        break
    print('Ошибка: отсуствует одна или две конструкции.')


name_lsit = input('список людей через запитую: ').split(', ')
ages_str = input('Возраст людей через пробел: ')
ages = [int(i_number) for i_number in ages_str.split()]

for i_man in range(len(name_lsit)):
    print(grats_temp.format(name=name_lsit[i_man], age=ages[i_man]))

people = [
    ' '.join([name_lsit[i_man], str(ages[i_man])])
    for i_man in range(len(name_lsit))
]

people_str = ', '.join(people)

print('\nИменинники: ', people_str)
