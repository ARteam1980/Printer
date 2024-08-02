import csv
with open("printer.csv", encoding='utf-8') as r_file:
    # Создаем объект DictReader, указываем ПРАВИЛЬНЫЙ! символ-разделитель ";"
    file_reader = csv.DictReader(r_file, delimiter = ";")
    # Считывание данных из CSV файла и выводим используя имена колонок
    for row in file_reader:
        print(f' {row["ID"]} - {row["IP"]} - {row["MAC"]} - {row["SN"]}')