# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n=input("-")
floats=[float(i) for i in n.split()]
results=[((i-int(i))) for i in floats]
print(round(max(results)-min(results), 3))
