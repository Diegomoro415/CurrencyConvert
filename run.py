# Import Library
from forex_python.converter import CurrencyRates, CurrencyCodes

# Create instance of CurrencyRates class
cr = CurrencyRates()

# Create instance of CurrencyCodes class
cc = CurrencyCodes()

# Define available currencies
currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD',
              'CHF', 'NZD', 'CNY', 'HKD', 'SGD', 'MXN',
              'SEK', 'NOK', 'DKK', 'TRY', 'ZAR', 'RUB',
              'INR', 'BRL', 'ARS', 'EGP', 'KRW', 'MYR',
              'THB', 'PHP', 'CLP', 'COP', 'IDR', 'NGN',
              'AED', 'BGN', 'HRK', 'CZK', 'HUF', 'ILS',
              'KWD', 'RON', 'SAR', 'VND', 'BTC', 'ETH',
              'BNB', 'ADA', 'XRP', 'SOL', 'DOT', 'DOGE',
              'UNI', 'LTC', 'MATIC', 'LINK', 'XLM', 'VET',
              'ATOM', 'AVAX', 'ALGO', 'FIL', 'TRX', 'BCH']


def top_currencies():
    print('\033[32m\n1-USD\n2-EUR\n3-GBP\n4-JPY\n5-CNY\n6-AUD\n7-HKD\n8-CAD\n'
          '9-BTC\n0-Others:\n\33[0;0m')


def label(txt):
    print('-'*len(txt))
    print('\033[34m'+txt+'\033[0;0m')
    print('-'*len(txt))


while True:
    # Instructions
    label('CURRENCY CONVERT')
    label('1- INSERT THE DESIRED VALUE TO EXCHANGE\n 2- \
 INSERT THE INITIAL CURRENCY\n 3- INSERT THE EXCHANGE CURRENCY')
    label('INSERT A VALUE')
    # Request user's input
    while True:
        try:
            amount = float(input('ENTER DESIRED AMOUNT TO BE CONVERTED:\n'))
            break
        except ValueError:
            print("\033[31m Input not valid!.  Insert a valid value\33[0;0m")
    # Insert intial currency
    label('PLEASE, SELECT THE INITIAL CURRENCY')
    currency_from = None
    while currency_from not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 0):
        top_currencies()
        try:
            currency_from = int(input("Select a currency:  "))
            if currency_from == 1:
                currency_from = 'USD'
                print("cod chosen:", currency_from)
                break
            elif currency_from == 2:
                currency_from = 'EUR'
                print("cod chosen:", currency_from)
                break
            elif currency_from == 3:
                currency_from = 'GBP'
                print("cod chosen:", currency_from)
                break
            elif currency_from == 4:
                currency_from = 'JPY'
                print("cod chosen:", currency_from)
                break
            elif currency_from == 5:
                currency_from = 'CNY'
                print("cod chosen:", currency_from)
                break
            elif currency_from == 6:
                currency_from = 'AUD'
                print("cod chosen:", currency_from)
                break
            elif currency_from == 7:
                currency_from = 'HKD'
                print("cod chosen:", currency_from)
                break
            elif currency_from == 8:
                currency_from = 'CAD'
                print("cod chosen:", currency_from)
                break
            elif currency_from == 9:
                currency_from = 'BTC'
                print("cod chosen:", currency_from)
                break
            elif currency_from == 0:
                currency_from = input(
                    '\nOthers, insert the currency code: (3 digits):').upper()
                print('Currency Code :', currency_from)
        except Exception:
            print(
                "\033[31m Input not valid!.  Choose a valid value :(\33[0;0m")
