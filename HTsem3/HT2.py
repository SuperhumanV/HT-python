# Напишите программу, которая найдёт произведение пар
# чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
import random
import numpy as np
def EnterMass():
    #Пользователь вводит максимальное число в массиве и его длину
   
    a = int(input('Enter max number of massive: '))
    b = int(input('Enter massive Length: '))
    return a,b


#Данные о массиве от пользователя
num, leng = EnterMass()
#заполнение списка и печать
mass = [random.randint(0, num)for _ in range(leng)]
print(mass)
#подсчет произведений
rez = np.array(mass)[len(mass)//2:][::-1]* np.array(mass)[:(len(mass))//2]
print(rez)