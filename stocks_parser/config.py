MONEYCONTROL = 'moneycontrol'
VALUE_RESEARCH = 'value_research'
DATE_FORMAT = 'date_format'
OUTPUT_FILE = 'outfile'
FIELDNAMES = 'fieldnames'

CSVKEY_SYMBOL = 'Symbol'
CSVKEY_PURCHASE_DATE = 'Purchase Date'
CSVKEY_BUY_QTY = 'Buy Quantity'
CSVKEY_BUY_PRICE = 'Buy Price'
CSVKEY_BUY_DATE = 'Buy Date'
CSVKEY_DATE = 'Date'
CSVKEY_UNITS = 'Units'
CSVKEY_ISIN_CODE = 'BSE/NSE/ISIN Code'
CSVKEY_BROKERAGE = 'Brokerage'
CSVKEY_TRANSACTION_TYPE = 'Transaction Type'
CSVKEY_TOTAL_AMOUNT = 'Total Amount'
CSVKEY_AMOUNT = 'Amount'

CONFIG = {
    MONEYCONTROL: {
        DATE_FORMAT: '%d/%m/%Y',
        OUTPUT_FILE: 'output/moneycontrol_formatted_trades.csv',
        FIELDNAMES: [CSVKEY_ISIN_CODE, CSVKEY_BUY_DATE, CSVKEY_BUY_QTY, CSVKEY_BUY_PRICE]
    },
    VALUE_RESEARCH: {
        DATE_FORMAT: '%d/%m/%Y',
        OUTPUT_FILE: 'output/valueresearch_formatted_trades.csv',
        FIELDNAMES: [CSVKEY_SYMBOL, CSVKEY_DATE, CSVKEY_UNITS, CSVKEY_BUY_PRICE, CSVKEY_BROKERAGE, CSVKEY_TRANSACTION_TYPE, CSVKEY_AMOUNT]
    }
}

STOCK_SYMBOLS = {
    'Adani Ports': 'ADANIPORTS',
    'Bajaj Auto Ltd': 'BAJAJ-AUTO',
    'Bharat Petroleum Corporation': 'BPCL',
    'Cipla Ltd': 'CIPLA',
    'Dr Reddys Laboratories Ltd': 'DRREDDY',
    'Hindustan Petroleum Corporation': 'HINDPETRO',
    'Hindustan Unilever Ltd': 'HINDUNILVR',
    'Infosys Ltd.': 'INFY',
    'ITC Ltd': 'ITC',
    'Reliance Industries Ltd': 'RELIANCE',
    'TATA Steel Limited': 'TATASTEEL',
    'Tata Consultancy Services Ltd': 'TCS',
    'Tech Mahindra Limited': 'TECHM',
    'JSW Steel': 'JSWSTEEL',
    'Larsen & Toubro': 'LT',
    'Sun Pharmaceutical': 'SUNPHARMA',
    'Tata Motors': 'TATAMOTORS',
    'Ramco Cements': 'RAMCOCEM',
    'DLF Ltd': 'DLF',
    'Housing Development': 'HDIL',
    'Mahindra': 'M&M',
    'NBCC': 'NBCC',
    'InterGlobe': 'INDIGO'
}