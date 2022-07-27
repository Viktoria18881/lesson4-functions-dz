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
def deposit_money(personal_score,money):

    while not money.isnumeric():
        input('Введите сумму: ')

    personal_score += int(money)
    print(f'Сумма на вашем счете: {personal_score}')
    return personal_score


def buy (personal_score, history, money):

    while not money.isnumeric():
        input('Введите сумму: ')

    money = int(money)

    if money > personal_score:
        print('Недостаточно средств')
    else:
        personal_score -= money
        history[input('Введите название товара: ')] = money

    return personal_score, history


def purchase_history(history):
    if len(history) > 0:
        print('История покупок: ')
        for key, val in history.items():
            print(f'{key} --> {val} ')
    else:
        print('Список пуст!')


personal_score = 0
history = {}

while True:
    print('1. пополнение счета')
    print ('2. покупка')
    print ('3. история покупок')
    print ('4. выход')

    choice = input('Выберите пункт меню:')
    if choice == '1':
        personal_score = deposit_money(personal_score, input('Введите сумму: '))
    elif choice == '2':
        personal_score, history = buy(personal_score, history, input('Введите сумму покупки: '))
    elif choice == '3':
        purchase_history(history)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
