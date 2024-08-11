# Дано:
numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Решение:
# 1. Воспользуемся библиотекой random. Напишем функцию для выбора случайного числа первой вставки (команда choice)
import random
def first_stone():
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    num = list(range(3, 21))
    stone_1 = random.choice(num)
    return stone_1

# 2. Напишем 2 цикла for для второй вставки.
# Главная сложность этой задачи - это обязательное переназначение переменных pairnumber_1 и pairnumber_2 в переменные
# циклов for i и j, потому что в ином случае n - это тип int, a pairnumber_1 и pairnumber_2 - тип list, действия с ними
# запрещены программой.

n = first_stone()

pairnumber_1 = list(range(1, n))
pairnumber_2 = list(range(1, n))
second_stone_pairs = []
result = ""

for i in pairnumber_1:
    for j in pairnumber_2:
        pn_1 = i
        pn_2 = j
# Для того, что пара начиналась с меньшего (!) числа и были выкинуты повторяющиеся пары, впишем доп.условие:
        if pn_1 >= pn_2:
            continue
# Основное решение:
        kratnost = n % (pn_1 + pn_2)
        if kratnost == 0:
            second_stone_pairs.append([pn_1, pn_2])
            result = result + str(pn_1) + str(pn_2)

# 3. Напечатаем полученные значения.
print("Шифр первой вставки: ", n)
print("Пары чисел: ", *second_stone_pairs)
print("Введите пароль во вторую вставку: ", result)
