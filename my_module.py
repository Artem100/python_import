from dirr import import_lesson2 # Если модуль который хотим импортиваровать находится в папке
# from import_lesson2 # Если модуль находится в корне проекта или в одной папке с модулем
import importlib

print(import_lesson2.factorial(10))
import_lesson2.num2 = 1000
print(import_lesson2.num2)

# Когда хотим обнулить значения для импортируемого класса
importlib.reload(import_lesson2)
print(import_lesson2.num2)