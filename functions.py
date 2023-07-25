import os
import sys
import shutil

def quiz():
    def year_question(year):
        while year != '1799':
            print("Не верно")
            year = input('Ввведите год рождения А.С.Пушкина:')
        pass

    def day_question(day):
        while day != '6':
            print("Не верно")
            day = input('В какой день июня родился Пушкин?')
        print('Верно')
        pass
        
    year = input('Ввведите год рождения А.С.Пушкина:')
    year_question(year)

    day = input('Ввведите день рождения Пушкин?')
    day_question(day)
def bank_amount():
    amount = 0
    purchases = {}
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            repleishment_amount = int(input('Введите сумму на которую хотите пополнить счет: '))
            amount += repleishment_amount
        
        elif choice == '2':
            purchases_sum = input('Введите сумму покупки: ')
            if purchases_sum.isdigit():
                if int(purchases_sum)> amount:
                    print('На покупку не хватает денег')
                if int(purchases_sum) <= amount:
                    purchare = input('Введите название покупки: ')
                    amount -= int(purchases_sum)
                    purchases[purchare]=purchases_sum
            else:
                print('Введено неверное значение')
        
        elif choice == '3':
            print(purchases)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
def create_folder():#1 пункт
    folder_name = input('Введите название папки: ')
    if not os.path.exists(f'D:/Python/Projects/python-004-console-file-manager/{folder_name}'):
        os.mkdir(f'D:/Python/Projects/python-004-console-file-manager/{folder_name}')
def delete_folder():#2 пункт
    deleted_folder_name = input('Введите название папки которую хотите удалить: ')
    if os.path.exists(f'D:/Python/Projects/python-004-console-file-manager/{deleted_folder_name}'):
        os.rmdir(f'D:/Python/Projects/python-004-console-file-manager/{deleted_folder_name}')
    else:
        print('Такой папки не существует')
def copy_file_or_folder():
    question = input('Вы хотите скопировать файл(1) или папку(2)? ')
    if question == '1':
        file_name = input('Введите название файла который хотите скопировать: ')
        if os.path.exists(f'D:/Python/Projects/python-004-console-file-manager/{file_name}'):
            shutil.copy(f'D:/Python/Projects/python-004-console-file-manager/{file_name}', f'D:/Python/Projects/python-004-console-file-manager/{file_name}_copy')
        else:
            print('Такого файла не существует')
    if question == '2':
        folder_name = input('Введите название файла который хотите скопировать: ')
        if os.path.exists(f'D:/Python/Projects/python-004-console-file-manager/{folder_name}'):
            shutil.copytree(f'D:/Python/Projects/python-004-console-file-manager/{folder_name}', f'D:/Python/Projects/python-004-console-file-manager/{folder_name}_copy')
        else:
            print('Такой папки не существует')
    else:
        print('Введено неверное значение')
def show_only_folders():
    for folders in os.listdir():
        if os.path.isdir(folders):
            print(folders)
def show_only_files():
    for file in os.listdir('D:/Python/Projects/python-004-console-file-manager'):
        if os.path.isdir(file) == False:
            print(file)