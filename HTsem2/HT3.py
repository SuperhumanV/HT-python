# Задайте список из (2*N+1) элементов, 
# заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. 
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.


import random
from functools import reduce

num = int(input('Enter your number: '))
seq = list(range(-num, num + 1))
indexes = [random.randint(0, num * 2)for  _ in range(5)]
print(reduce(lambda x,y: x*y, [seq[i]for i in indexes]))
