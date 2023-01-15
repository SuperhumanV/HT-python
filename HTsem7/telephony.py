#Создать телефонный справочник с возможностью импорта 
# и экспорта данных в нескольких форматах.
#под форматами понимаем структуру файлов, например:
# в файле на одной строке хранится одна часть записи,
#  пустая строка - разделитель
#Фамилия_1 Имя_1 Телефон_1 Описание_1
#Фамилия_2 Имя_2 Телефон_2 Описание_2
#и т.д.в файле на одной строке хранится все записи, 
# символ разделитель - ;**
#Фамилия_1,Имя_1,Телефон_1,Описание_1
#Фамилия_2,Имя_2,Телефон_2,Описание_2

COLUMNS = ['Фамилия', 'Имя', 'Номер телефона', 'Описание']
def add_row():
     return [input(f"Введите: {i}: ") for i in COLUMNS]

def write(arr):
    with open("file_1.txt", "a") as f:
        f.write(", ".join(arr) + "\n")

def write_one_column(arr):
    with open("file_2.txt", "a") as f:
        for value in arr:
            f.write(value + "\n")
        f.write("\n")

def read(path):
    with open(path, "r") as f:
        return [i.split(", ") for i in f.read().strip().split("\n")]

def print_data(arr):
    print(", ".join(COLUMNS))
    for i in arr:
        print(", ".join(i))

for _ in range(2):
    row = add_row()
    write(row)
    write_one_column(row)

print_data(read("file_1.txt"))
