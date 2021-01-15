"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""
from random import randrange


with open('task5_txt.txt', 'w+', encoding='UTF-8') as file:
    file.write(' '.join([str(randrange(100)) for i in range(25)]))
    file.seek(0)
    line = file.readline()
    print(sum([int(x) for x in line.split()]))
