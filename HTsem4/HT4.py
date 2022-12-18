# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать 
# в файл (или вывести в терминал) многочлен степени k.
import random
k = random.randint(0, 100)
mngch = "+".join(
    [f"{i}*x^{k}" if k>1 else
    f"{i}*x" if k>0 else
    f"{i}"
    for k,i in enumerate([random.randint(0, 100)for i in range(k+1)])
    if i !=0][::-1]
)

print(k)
print(mngch)
data = open('HomeTasks/HTsem4/mnogochlen.txt','a')
data.writelines(f'\n{mngch}\n')