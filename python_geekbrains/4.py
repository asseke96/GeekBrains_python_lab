'''
4.Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки нужно пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
'''

stroka = input()
stroka_list = stroka.split(' ')

for i in range(1,len(stroka_list)):
    if len(stroka_list[i-1]) <=10:
        print(i,stroka_list[i-1])
    else:
        print(i,stroka_list[i-1][:10])