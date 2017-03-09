import os
import csv
from config import *

input_csv_file = 'input/profit_loss_statement.csv'
input_xlsx_file = 'input/profit_loss_statement.xlsx'


def convert_xls_to_csv(xlsfile, csvfile):
    os.system('in2csv {} > {}'.format(xlsfile, csvfile))

def build_data_store(csvfile):
    clean_buffer = _clean_csv(csvfile)
    fields, data = clean_buffer[0].split(','), clean_buffer[1:]
    csv_buffer = list(_parse_data(fields, data))

    for key in [GOOGLE_FINANCE, MONEYCONTROL]:
        conf = CONFIG[key]
        with open(conf[OUTPUT_FILE], 'w') as output_csv:
            writer = csv.DictWriter(output_csv, fieldnames=conf[FIELDNAMES], extrasaction='ignore')
            writer.writeheader()
            writer.writerows(csv_buffer)


def _parse_data(fields, data):
    for d in data:
        d = map(str.strip, d.split(','))
        mapping = dict(zip(fields, d))
        yield _create_struct(mapping)

def _create_struct(mapping):
    stock_symbol = STOCK_SYMBOLS[mapping['Name']]
    buy_date = mapping['Purc Date']
    qty = int(mapping['Purc Qty'])
    price_for_all = float(mapping['Purc Value'])
    price_per = '{0:.2f}'.format(price_for_all/qty)
    brokerage = '{0:.2f}'.format(float(mapping['Charges']) + float(mapping['STT']))
    return {
        CSVKEY_ISIN_CODE: stock_symbol,
        CSVKEY_SYMBOL: 'NSE:' + stock_symbol,
        CSVKEY_PURCHASE_DATE: buy_date,
        CSVKEY_BUY_DATE: buy_date,
        CSVKEY_BUY_QTY: qty,
        CSVKEY_BUY_PRICE: price_per,
        CSVKEY_BROKERAGE: brokerage
    }

def _clean_csv(csvfile):
    STOCK_NAMES = STOCK_SYMBOLS.keys()
    def _is_useful_data(line):
        if 'Gain' in line and 'Charges' in line:
            return True
        for stock_name in STOCK_NAMES:
            if stock_name in line:
                return True
        return False

    with open(csvfile, 'r') as lines:
        return filter(_is_useful_data, lines)

if __name__ == '__main__':
    convert_xls_to_csv(input_xlsx_file, input_csv_file)
    build_data_store(input_csv_file)

# build a name => Symbol map iin conf.py