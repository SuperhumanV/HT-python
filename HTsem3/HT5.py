# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
k =int(input('enter number '))
def fibo_bog():
    rez = []
    for i in range(k):
        if i == 0:
            rez.append(0)
        elif i == 1:
            rez.append(1)
        else:
            rez.append(rez[i-1]+ rez[i-2])
    return rez

num  = fibo_bog()
rez = [-num[i]if i%2==0 else num[i]for i in range(k)][:0:-1]+num
print(rez)