"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

with open('task2_txt.txt', 'r', encoding='UTF-8') as file:

    lines = file.readlines()
    print('Количество строк в файле: ', len(lines))

    for idx, word in enumerate(lines, 1):
        print(f'В {idx} строке находится {len(word.split())} слов')
