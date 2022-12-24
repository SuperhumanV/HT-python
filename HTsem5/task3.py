# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Восстановить
# Ввёл: stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"

from itertools import groupby, repeat

def Zip(string):
    
    #RLE compression
    return "".join( 
        "".join( (str(sum(1 for _ in g)), k) ) 
            for k, g in groupby(string) 
    )

def unZip(string):
    
    #RLE decompression
    return "".join(
        "".join(repeat(string[i+1], int(string[i]))) 
            for i in range(0, len(string), 2)
    )

def read(path):
    with open(path, "r") as f:
        return f.read().strip()
    
def write(path,string):
    with open(path, "w") as f:
        f.write(string)


string = read("HomeTasks/HTsem5/string.txt")
string = Zip('aaabbbbccbbb')
write("HomeTasks/HTsem5/zip.txt", string)
string = unZip(string)
write("HomeTasks/HTsem5/unzip.txt", string)
