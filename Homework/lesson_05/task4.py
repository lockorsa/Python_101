""" 4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('task4_txt.txt', 'r', encoding='UTF-8') as source_file:
    with open('task4_2_txt.txt', 'w', encoding='UTF-8') as destination_file:
        lines = source_file.readlines()
        for line in lines:
            line = line.split()
            line[0] = translation[line[0]]
            line.append('\n')
            destination_file.write(' '.join(line))
