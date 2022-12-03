def input_k(x):
    xyz = ['X','Y','Z']
    a = []
    for i in range(x):
        a.append(int(input(f'Введите значение {xyz[i]} ')))
    return a

def TorF(x):
    first = not (x[0] or x[1] or x[2])
    second = not x[0] and not x[1] and not x[2]
    result = first == second
    return result

INDEX = input_k(3)

if TorF(INDEX) == True:
    print('Верно')
else:
    print('Ошибочно')