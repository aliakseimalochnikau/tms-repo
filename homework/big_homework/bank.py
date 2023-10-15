from random import randint
import json
import os

'''
Функция get_random_digits() была модифицирована.
Теперь она принимает в качестве опционального аргумента separator, который служит для разделения цифр на блоки по 4
для лучшей визуализации. По умолчанию равняется пустой строке.
'''


def get_random_digits(count, separator='') -> str:
    result = ''
    counter = 0
    for _ in range(count):
        result += str(randint(0, 9))
        counter += 1
        if counter % 4 == 0:
            result += separator
    return result.rstrip()


class BankAccount:
    def __init__(self, card_holder, currency, money=0.00, card_number=None, account_number=None):
        self.card_holder = card_holder.upper()
        self.currency = currency.upper()  # Добавлено новое поле "валюта"
        self.money = money
        self.account_number = get_random_digits(20) if account_number is None else account_number
        self.card_number = get_random_digits(16, separator=' ') if card_number is None else card_number


def convert_bank_account_to_dict(account: BankAccount) -> dict:
    bank_account = {
        'card_holder': account.card_holder,
        'currency': account.currency,
        'money': account.money,
        'card_number': account.card_number,
        'account_number': account.account_number
    }
    return bank_account


def save_accounts(bank_accounts: dict[str, BankAccount], file_name):
    data = {}
    for account_number, bank_account in bank_accounts.items():
        data[account_number] = convert_bank_account_to_dict(bank_accounts[account_number])
    with open(file_name, 'w') as file:
        json.dump(data, file)


def load_accounts(file_name) -> dict[str, BankAccount]:
    data = {}
    if not os.path.exists(file_name):
        return {}
    with open(file_name) as file:
        loaded_data = json.load(file).items()
        for account_number, bank_account_data in loaded_data:
            data[account_number] = BankAccount(**bank_account_data)
    return data


class Bank:
    def __init__(self, bank_accounts=None):
        self.bank_accounts: dict[str, BankAccount] = bank_accounts if bank_accounts is not None else {}

    def open_account(self, card_holder, currency):
        account = BankAccount(card_holder, currency)
        self.bank_accounts[account.account_number] = account
        return account

    #  Добавлена функция check_balance() для проверки баланса по номеру счёта
    def check_balance(self, account_number):
        balance = self.bank_accounts[account_number].money
        return balance

    def add_money(self, account_number, money):
        account = self.bank_accounts[account_number]
        account.money += money

    def transfer_money(self, from_account_number, to_account_number, money, conversion_rate):
        from_account = self.bank_accounts[from_account_number]
        to_account = self.bank_accounts[to_account_number]
        from_account.money -= money
        to_account.money += money * conversion_rate

    def external_transfer(self, from_account_number, to_external_number, currency, money):
        self.bank_accounts[from_account_number].money -= money
        print(f'Банк успешно перевёл {currency} {money:,.2f} с вашего счёта {from_account_number} на внешний счёт'
              f' {to_external_number}')


"""
Добавлен класс CurrencyConverter и метод conversion_rate_selector() для осуществления конверсии валют в случае,
если при переводе валюта счета отправителя не совпадает с валютой счета получателя
"""


class CurrencyConverter:
    def __init__(self):
        self.__conversion_rates: dict[str, float] = {
            'eur_to_usd': 1.0588,
            'usd_to_eur': 0.9443,
            'gbp_to_usd': 1.2257,
            'usd_to_gbp': 0.8157,
            'gbp_to_eur': 1.1575,
            'eur_to_gbp': 0.8637
        }

    def conversion_rate_selector(self, from_currency, to_currency):
        if from_currency == 'USD' and to_currency == 'EUR':
            return self.__conversion_rates['usd_to_eur']
        elif from_currency == 'USD' and to_currency == 'GBP':
            return self.__conversion_rates['usd_to_gbp']
        elif from_currency == 'EUR' and to_currency == 'USD':
            return self.__conversion_rates['eur_to_usd']
        elif from_currency == 'EUR' and to_currency == 'GBP':
            return self.__conversion_rates['eur_to_gbp']
        elif from_currency == 'GBP' and to_currency == 'USD':
            return self.__conversion_rates['gbp_to_usd']
        elif from_currency == 'GBP' and to_currency == 'EUR':
            return self.__conversion_rates['gbp_to_eur']


class Controller:
    def __init__(self, data_file_name):
        self.data_file_name = data_file_name
        bank_accounts: dict[str, BankAccount] = load_accounts(data_file_name)
        self.bank = Bank(bank_accounts)

    def show_open_accounts(self):
        print(f'В настоящее время открыто счетов: {len(self.bank.bank_accounts.items())}')
        for account_number, bank_account_data in self.bank.bank_accounts.items():
            print('=' * 35)
            print(f'Номер счёта: {account_number}')
            print(f'Держатель счёта: {bank_account_data.card_holder}')
            print(f'Валюта счёта: {bank_account_data.currency}')
            print(f'Баланс счёта: {bank_account_data.money:,.2f}')
            print(f'Номер карты: {bank_account_data.card_number}')
            print()

    def run(self):
        print('Здравствуйте, наш банк открылся!')
        while True:
            print('Выберите действие: ')
            print('0. Завершить программу')
            print('1. Открыть новый счёт')
            print('2. Посмотреть открытые счета')
            print('3. Пополнить счёт')
            print('4. Осуществить перевод средств между счетами')
            print('5. Совершить платёж')
            print('6. Проверить баланс счёта')

            action = int(input())
            match action:

                case 0:
                    print('Спасибо, что воспользовались услугами нашего банка. До свидания!')
                    save_accounts(self.bank.bank_accounts, self.data_file_name)
                    break

                case 1:
                    card_holder = input('Введите имя и фамилию держателя счёта на английском языке:\n')
                    currency = input('Введите код валюты, в которой желаете открыть счёт (USD, EUR, GBP):\n')
                    account = self.bank.open_account(card_holder, currency)
                    print(f'Создан счёт: {account.account_number}')
                    print(f'Валюта счёта: {account.currency}')
                    print(f'Эмитирована карта: {account.card_number}')

                case 2:
                    self.show_open_accounts()

                case 3:
                    account = input('Введите номер счёта, который следует пополнить:\n')
                    currency = self.bank.bank_accounts[account].currency
                    money = float(input(f'Введите сумму пополнения ({currency}):\n'))
                    self.bank.bank_accounts[account].money += money
                    print(f'Cчёт {account} был пополнен на сумму {currency} {money:,.2f}')

                case 4:
                    from_account_number = input('Введите Ваш номер счёта:\n')
                    to_account_number = input('Введите номер счёта получателя перевода:\n')
                    from_currency = self.bank.bank_accounts[from_account_number].currency
                    to_currency = self.bank.bank_accounts[to_account_number].currency
                    money = float(input(f'Введите сумму перевода ({from_currency}):\n'))
                    conversion_rate = 1.0
                    if from_currency != to_currency:
                        converter = CurrencyConverter()
                        conversion_rate = converter.conversion_rate_selector(from_currency, to_currency)
                        print(f'Была произведена конверcия по курсу 1 {from_currency} ='
                              f' {1 * conversion_rate} {to_currency}')
                    self.bank.transfer_money(from_account_number, to_account_number, money, conversion_rate)
                    print(f'Перевод успешно завершён')
                    print(f'Сумма перевода: {from_currency} {money:,.2f}')
                    print(f'На счёт {to_account_number} зачислено {to_currency} {money * conversion_rate:,.2f}')

                case 5:
                    from_account_number = input('Введите Ваш номер счёта:\n')
                    to_external_number = input('Введите номер счёта получателя платежа:\n')
                    currency = self.bank.bank_accounts[from_account_number].currency
                    money = float(input(f'Введите сумму платежа ({currency}):\n'))
                    self.bank.external_transfer(from_account_number, to_external_number, currency, money)

                case 6:
                    account = input('Введите Ваш номер счёта:\n')
                    balance = self.bank.check_balance(account)
                    currency = self.bank.bank_accounts[account].currency
                    print(f'Текущий баланс счёта {account}: {currency} {balance:,.2f}')

                case _:
                    print('Неверная операция')


if __name__ == '__main__':
    controller = Controller('data.json')
    controller.run()
