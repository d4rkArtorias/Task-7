from functions.functions import *
while True:
    
    print('1. Создать папку')
    print('2. Удалить файл/папку')
    print('3. Копировать файл/папку')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Выход')
    
    choise = input('Выберите пункт меню: ')
    if choise == '1':
        create_folder()
    if choise == '2':
        delete_folder()
    if choise == '3':
        copy_file_or_folder()
    if choise == '4':
        wd = os.listdir('D:/Python/Projects/python-004-console-file-manager')
        print(wd)
        with open ('work_directory.txt', 'w', encoding='utf-8') as work_directory:
            for folders in os.listdir():
                if os.path.isdir(folders):
                    work_directory.writelines(f'folders: {folders}')
                else:
                    work_directory.write(f'\nfiles: {folders}')
    if choise == '5':
        show_only_folders()
    if choise == '6':
        show_only_files()
    if choise == '7':
        print(sys.platform)
    if choise == '8':
        print('Artorias-san')
    if choise == '9':
        quiz()
    if choise == '10':
        bank_amount
    if choise == '11':
        break