import calendar # Импортировать весь модуль календарь (систеная утилита)
# import math as m # Импортировать модуль и задать уме пседоним в коде

from math import e, pi # когда хотим импортировать только определенные функции или классы
from math import * # импортировать все имена (лучше никогда не импортивать так)
from math import e, factorial as fact # импортировать определенные имена и одну функцию задать как псевдоним

def say_hello(name):
    print(f"Hi, {name}")

def summa(*args):
    return sum(args)

def factorial (n):
    pr = 1
    for i in range(1, n+1):
        pr*=i
    return pr

my_srt = "Test string"
num1 = 1
num2 = 3


c = calendar.TextCalendar() # в экзмепляр передать класс TextCalendar
print(c.formatmonth(2021, 10)) # Вызываем функцию класса
# print(m.e) # Обращение через псевдоним
print(e) # Обращение напрямую
print(fact(10)) # Обращение к функции как к псевдониму
