#first lesson

'''
x = 2 
y = 3 
z = x + y 
print(z) # вывод результата в консоль
'''

'''
greetings = "Hello World"
print(greetings)
'''

'''
age = 33
print("my_age_is:", age)
'''

#2th lesson


'''
name = input('Введите Ваше Имя: ') # Ввод данных
print('Привет,', name)
'''

'''
#Типы данных
a = 5 #число: int()
b = 5.5 #число с точкой: float()
с = '9.6' #строка: str()
'''

'''
# Калькулятор
x = int(input())
y = int(input())
print(x + y)
'''

#3th lesson

'''
print(23 / 7) #обычное деление
print(23 // 7) #деление без остатка
print(23 % 7) #деление по остатку
'''

'''
import math
print(math.log(5, 10) + math.log(2, 10))
'''

'''
number = int(input())
thousand = number // 1000 # находим первую цифру
hundred = number % 1000 // 100 # находим вторую цифру
ten = number % 100 // 10 # находим третью цифру
one = number % 10 # находим четвертую цифру
print(f'Цифра позиции тысяч равна {thousand}')
print(f'Цифра позиции сотен равна {hundred}')
print(f'Цифра позиции десятков равна {ten}')
print(f'Цифра позиции едениц равна {one}')
'''

#4th lesson

'''
# оператор сравнения
answer = input('Какой сейчас год?: ')
if answer == '2024':
    print('Right!')
else:
    print('NO!')
    2
print('Program complited')
'''

#5th lesson

'''
# Тернарный оператор
true_value if condition else false_calue
'''

'''
#elif
day = int(input())
if day == 1:
    print('monday')
elif day ==2:
    print('truesday')
elif day == 3:
    print('wednesday')
elif day == 4:
    print('thursday')
elif day == 5:
    print('friday')
elif day == 6:
    print('saturday')
elif day == 7:
    print('sunday')
else:
    print('error')
'''

#6th lesson

'''
# Вложенный оператор
login = input()

if login == 'admin':
    print('Логин введен верно!')
    password = input()
    if password == '123':
        print('пароль введен верно!')
    else:
        print('пароль введен неверно!')
else:
    print('Логин введен неверно!')
'''

#7th lesson

'''
# Цикл for
for i in range(3):
    for j in range(5):
        for k in range(7):
            print(i, j, k)
'''