#Получаем цифру дня недели
day = int(input('Enter the day of week number '))
#цикл для проверки выходной или будний
if 0<day<6:
    print('Будний день ')
elif 8>day>5:
    print('Выходной ')
else:
    print('INVALID DATA')



