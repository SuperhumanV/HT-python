x = int(input('Введите координаты по x '))
y = int(input('Введите координаты по y '))
if x != 0 and y !=0 :
    if x > 0 and y > 0:
        print('1 квадрат')
    elif x > 0 and y < 0:
        print('2 Квадрат')
    elif x < 0 and y < 0:
        print('3 квадрат')
    else:
        print('4 квадрат')
else:
    print('INVALID INPUT')
