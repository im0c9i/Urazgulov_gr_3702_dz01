# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x_coordinat_A = float(input('Введите координату х точки А: '))
y_coordinat_A = float(input('Введите координату y точки А: '))
x_coordinat_B = float(input('Введите координату х точки B: '))
y_coordinat_B = float(input('Введите координату y точки B: '))
import math
distanse = round(math.sqrt((x_coordinat_B - x_coordinat_A)**2 + (y_coordinat_B - y_coordinat_A)**2),2)
print(distanse)
