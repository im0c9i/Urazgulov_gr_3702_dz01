# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


numX = int(input('Введите координату х: '))
numY = int(input('Введите координату y: '))

def koordinat(numX, numY):
    if numX != 0 and numY != 0:
        if numX*numY > 0:
            if numX > 0:
                return 'I четверть'
            else:
                return 'III четверть'
        else:
            if numX > 0:
                return 'IV четверть'
            else:
                return 'II четверть'
    else:
        if numX == 0:
            return 'oY'
        else:
            return 'oX'

print(koordinat(numX, numY))
