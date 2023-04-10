"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

"Без генератора"

import random

list1 = random.sample(range(1, 1000), 20)  # генерирует числа от 1 до 1000, всего этих чисел 20
print(list1)
list2 = []
for el in range(len(list1) - 1):
    if list1[el] < list1[el + 1]:
        list2.append(list1[el + 1])
print(list2)

"С генератором"

result_list = []
list = [int(i) for i in input("Введите чисела разделяя их пробелом: ").split()]
for i in range(1, len(list)):
    if list[i] > list[i - 1]:
        (result_list.append(list[i]))
print("Исходный список: ", list)
print("Список, элементы которого больше предыдущего: ", result_list)
