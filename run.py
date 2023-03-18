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
