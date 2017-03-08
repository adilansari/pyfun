GOOGLE_FINANCE = 'gfinance'
MONEYCONTROL = 'moneycontrol'
DATE_FORMAT = 'date_format'
OUTPUT_FILE = 'outfile'
FIELDNAMES = 'fieldnames'

CSVKEY_SYMBOL = 'Symbol'
CSVKEY_PURCHASE_DATE = 'Purchase Date'
CSVKEY_BUY_QTY = 'Buy Quantity'
CSVKEY_BUY_PRICE ='Buy Price'
CSVKEY_BUY_DATE = 'Buy Date'
CSVKEY_ISIN_CODE = 'BSE/NSE/ISIN Code'

CONFIG = {
    GOOGLE_FINANCE: {
        DATE_FORMAT: '%m/%d/%Y',
        OUTPUT_FILE: 'output/gfinance_formatted_trades.csv',
        FIELDNAMES: [CSVKEY_SYMBOL, CSVKEY_PURCHASE_DATE, CSVKEY_BUY_QTY, CSVKEY_BUY_PRICE]
    },
    MONEYCONTROL: {
        DATE_FORMAT: '%d/%m/%Y',
        OUTPUT_FILE: 'output/moneycontrol_formatted_trades.csv',
        FIELDNAMES: [CSVKEY_ISIN_CODE, CSVKEY_BUY_DATE, CSVKEY_BUY_QTY, CSVKEY_BUY_PRICE]
    }
}