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

        # Select a currency to exchage value
        label('SELECT THE CONVERSION CURRENCY')
        currency_to = None
        while currency_to not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 0):
            top_currencies()
            try:
                currency_to = int(input("Select a currency:  "))
                if currency_to == 1:
                    currency_to = 'USD'
                    print("cod chosen:", currency_to)
                    break
                elif currency_to == 2:
                    currency_to = 'EUR'
                    print("cod chosen:", currency_to)
                    break
                elif currency_to == 3:
                    currency_to = 'GBP'
                    print("cod chosen:", currency_to)
                    break
                elif currency_to == 4:
                    currency_to = 'JPY'
                    print("cod chosen:", currency_to)
                    break
                elif currency_to == 5:
                    currency_to = 'CNY'
                    print("cod chosen:", currency_to)
                    break
                elif currency_to == 6:
                    currency_to = 'AUD'
                    print("cod chosen:", currency_to)
                    break
                elif currency_to == 7:
                    currency_to = 'HKD'
                    print("cod chosen:", currency_to)
                    break
                elif currency_to == 8:
                    currency_to = 'CAD'
                    print("cod chosen:", currency_to)
                    break
                elif currency_to == 9:
                    currency_to = 'BTC'
                    print("cod chosen:", currency_to)
                    break
                elif currency_to == 0:
                    currency_to = input(
                        '\nOthers, insert currency code: (3 digits):').upper()
                    print('Currency Code :', currency_to)
                    break
            except Exception:
                print(
                    "\033[31m Input not valid!. Try again :(\33[0;0m")
                # Check if user choose currencies are available
                if currency_from or currency_to not in currencies:
                    print('Invalid input. The available currencies are: ')
                    print(currencies)
                    continue
        # Conversion
        label('CONVERTING...')
        # Get the exchange rate between currencies
        result = cr.get_rate(currency_from, currency_to, amount)
        # Get the exchange rate between currencies
        exchange_rate = cr.get_rate(currency_from, currency_to)
        # Format the output
        symbol_from = cc.get_symbol(currency_from)
        symbol_to = cc.get_symbol(currency_to)
        result = round(result, 2)
        print(f'{currency_from}  -  {symbol_from} {amount} '
              f' =========================== '
              f' {currency_to}  -  {symbol_to} { result} '
              f' Exchange rate: {exchange_rate:.4f})')
        # Ask if user wants to perform another conversion
        answer = input('Do you wish to perform another time? (Y/N): ').upper
        if answer == 'N':
            break
