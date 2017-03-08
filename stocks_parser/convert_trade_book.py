import csv
import time
from config import *

# read the input file into a dict
# parse that dict into a new dict only keeping the needed fields
# dump this new dict into a csv

def convert(input_file):

    with open(input_file) as input_csv:
        reader = csv.DictReader(input_csv)
        output_data = list(map(_filter_noise, reader))


    for key in [GOOGLE_FINANCE, MONEYCONTROL]:
        conf = CONFIG[key]
        with open(conf[OUTPUT_FILE], 'w') as output_csv:
            writer = csv.DictWriter(output_csv, fieldnames=conf[FIELDNAMES], extrasaction='ignore')
            writer.writerows(output_data)

def _filter_noise(row):
    return {
        CSVKEY_ISIN_CODE: row['Symbol '].strip(),
        CSVKEY_SYMBOL: 'NSE:' + row['Symbol '].strip(),
        CSVKEY_PURCHASE_DATE: time.strftime(CONFIG[GOOGLE_FINANCE][DATE_FORMAT]),
        CSVKEY_BUY_DATE: time.strftime(CONFIG[MONEYCONTROL][DATE_FORMAT]),
        CSVKEY_BUY_QTY: int(row['Quantity '].strip()),
        CSVKEY_BUY_PRICE: float(row['Price '].strip())
    }

if __name__ == "__main__":
    input_file = "input/trade_book.csv"
    convert(input_file)
