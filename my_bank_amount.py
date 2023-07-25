amount = 0
purchases = {}
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. добавить сохранение суммы счета в файл')
    print('5. добавить сохранение истории покупок в файл')
    print('6. выход')
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
        with open('amount_sum.txt', 'w', encoding='utf-8') as amount_sum:
            amount_sum.write(f'Сумма счета: {amount}\n')
    elif choice == '5':
        with open('order_history.txt', 'w', encoding='utf-8') as order_history:
            order_history.write(f'История покупок: {purchases}')
    elif choice == '6':
        break
    else:
        print('Неверный пункт меню')
