"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import re # импортируем библиотеку регулярных выражений

online = True    # переменная для запуска/остановки программы
amount_total = 0.0    # переменная с общей суммой на счете
purchase_list = []    # список покупок
symbl = '#'*5    # универсальный разделитель

# функция проверки ввода пользователя на число int/float
def is_number(x):
    try:
        float(x)
        return True

    except ValueError:
        return False

# пока переменная запуска/остановки программы будет в положении True, код будет выполняться по кругу
while online:

    # выводим пункты меню
    print('ПУНКТЫ МЕНЮ:')
    print('Пополнение счета --> 1')
    print('Покупка --> 2')
    print('История покупок --> 3')
    print('Выход из программы --> 4\n')

    # запрашиваем выбор пользователем пункта меню
    choice = input('Выберите пункт меню:')

    # если пользователь выбирает 'Пополнение счета', то с помощью регулярных выражений меняем ',' на '.' в случае, если
    # используется кириллическая раскладка
    # проверяем введено ли число, если нет - просим пользователя повторить ввод, если число - пополняем счет и выводим
    # сообщение об общей сумме на счете
    if choice == '1':
        amount_add = re.sub(r'[,]', '.', input(f'{symbl} На какую сумму вы хотите пополнить счет? Введите сумму: '))
        while not is_number(amount_add):
            amount_add = re.sub(r'[,]', '.', input(f'{symbl} Извините, произошла ошибка. Введите сумму для пополнения счета: '))
        amount_total += float(amount_add)
        print(f'{symbl} На вашем счете {amount_total} у.е.\n')

    # если пользователь выбрал 'Покупка', то запрашиваем стоимость покупки, проверяем ее на число и с помощью регулярных
    # выражений меняем ',' на '.' в случае, если используется кириллическая раскладка
    elif choice == '2':
        purchase_amount = re.sub(r'[\D]', '.', input(f'{symbl} Сколько вам требуется у.е. на покупку? Введите сумму: '))
        while not is_number(purchase_amount):
            purchase_amount = re.sub(r'[\D]', '.',input(f'{symbl} Извините, произошла ошибка. Введите сумму для покупки: '))

        # если средств на счете недостаточно, то выводим сообщение о необходимости пополнить счет и сумме на счете
        if float(purchase_amount) > amount_total:
            print(f'{symbl} Извините, у вас недостаточно средств для покупки на {purchase_amount} у.е. На вашем счете '
                  f'сейчас {amount_total} у.е. Пополните счет не менее чем на {purchase_amount-amount_total}.\n')

        # если средств достаточно, то запрашиваем что пользватель хочет купить
        # стоимость покупки вычитаетаем из суммы на счете
        # информацию о покупке (что и за сколько) записываем в список множеством
        # выводим информацию, что покупка совершена и сумме на счете
        else:
            purchase_name = input(f'{symbl} Что вы хотите купить? Введите название покупки: ')
            purchase_amount = float(purchase_amount)
            amount_total -= purchase_amount
            purchase_list.append((purchase_name, purchase_amount))
            print(f'{symbl} Покупка совершена. На вашем счете {amount_total} у.е.\n')

    # если пользователь выбрал 'История покупок', то проверяем, есть ли покупки у пользователя
    # если покупок нет - выводим сообщение об этом
    # если покупки есть, то в цикле выводим через разделитель '-->' что куплено и за сколько
    # за счет использования множеств в истории покупок сохраняются покупки, даже если они идентичны по названию и/или
    # стоимости
    elif choice == '3':
        print(f'{symbl} История ваших покупок:')
        if len(purchase_list) < 1:
            print(f'{symbl} У вас пока не было покупок. На вашем счете {amount_total} у.е.')
            print(f'{symbl} КОНЕЦ ИСТОРИИ ПОКУПОК\n')
        else:
            for i in purchase_list:
                print(f'{symbl} {i[0]} --> {i[1]}')
            print(f'{symbl} КОНЕЦ ИСТОРИИ ПОКУПОК\n')

    # если пользователь выбрал 'Выход из программы', то переводим переключатель в положение False и прощаемся с
    # пользователем
    elif choice == '4':
        print(f'{symbl} До новых встреч!')
        online = False

    # если пользователь ввел что-то кроме 1-4, то сообщаем ему об ошибке и предлагаем повторить ввод
    else:
        print('Неверный пункт меню\n')
