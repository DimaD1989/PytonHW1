# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# a = int(input ('Введите день недели a: '))
# if(a == 6 or a == 7):
#     print ('Ура,этот день выходной')
# elif(a< 1 or a > 7):
#     print ('Это вообще не день недели')
# else:
#     print ('Этот день не выходной -> нет')

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3





# Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = int(input ('Введите x1: '))
y1 = int(input ('Введите y1: '))
x2 = int(input ('Введите x2: '))
y2 = int(input ('Введите y2: '))
S=((x2-x1)**2+(y2-y1)**2)** (0.5)
print('{:2f}'.format(S),sep='')




