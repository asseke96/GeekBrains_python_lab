'''
2. Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов нужно использовать функцию input().
'''

n = int(input('Введите кол-во элементов списка: '))
massiv = [0]*n

for i in range(n):
    massiv[i] = input()
print('Список до перестановки: ',massiv)

for i in range(1,len(massiv),2):
    massiv[i-1],massiv[i] = massiv[i],massiv[i-1]

print('Список после перестоновки: ',massiv)

