import csv

users = [
    ['Tom', 16],
    ['Tim', 19],
    ['Alice', 22],
]

with open('users.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(users)

user3 = ['Sam', 25]
with open('users.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(user3)

# Считывание из другого файла. Скачиваем файл в репозиторий

with open('название файла.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])
