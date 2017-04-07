import os
import csv
from config import *
from datetime import datetime

input_csv_file = 'input/profit_loss_statement.csv'
input_xlsx_file = 'input/profit_loss_statement.xlsx'
STOCK_NAMES = STOCK_SYMBOLS.keys()


def convert_xls_to_csv(xlsfile, csvfile):
    os.system('ssconvert {} {}'.format(xlsfile, csvfile))


def build_data_store(csvfile):
    data_store = []

    with open(csvfile, 'r') as lines:
        cached_stock_name = ''
        for line in lines:
            stock_name = _extract_stock_name(line)
            if stock_name:
                cached_stock_name = stock_name
                continue
            data = line.split(',')
            date = _extract_date(data[4])
            if not date:
                continue
            data_store.append(_extract_stock_info(cached_stock_name, data))
            cached_stock_name = ''

    return data_store


def _extract_stock_info(stock_name, array):
    temp_buffer = dict()
    temp_buffer['symbol'] = stock_name
    temp_buffer['date'] = _extract_date(array[4])
    temp_buffer['qty'] = int(array[5])
    temp_buffer['price_per'] = float(array[6])
    temp_buffer['charges'] = float(array[15])
    temp_buffer['stt'] = float(array[21])
    return temp_buffer


def _extract_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y/%d/%m")
    except ValueError:
        return None


def _extract_stock_name(line):
    for name, symbol in STOCK_SYMBOLS.items():
        if name in line:
            return symbol
    return None


def generate_output_csv(filtered_data):
    csv_buffer = map(_create_struct, filtered_data)

    for key in [GOOGLE_FINANCE, MONEYCONTROL]:
        conf = CONFIG[key]
        with open(conf[OUTPUT_FILE], 'w') as output_csv:
            writer = csv.DictWriter(output_csv, fieldnames=conf[FIELDNAMES], extrasaction='ignore')
            writer.writeheader()
            writer.writerows(csv_buffer)


def _create_struct(mapping):
    stock_symbol = mapping['symbol']
    brokerage = '{0:.2f}'.format(float(mapping['charges']) + float(mapping['stt']))
    return {
        CSVKEY_ISIN_CODE: stock_symbol,
        CSVKEY_SYMBOL: 'NSE:' + stock_symbol,
        CSVKEY_PURCHASE_DATE: mapping['date'].strftime(CONFIG[GOOGLE_FINANCE][DATE_FORMAT]),
        CSVKEY_BUY_DATE: mapping['date'].strftime(CONFIG[MONEYCONTROL][DATE_FORMAT]),
        CSVKEY_BUY_QTY: int(mapping['qty']),
        CSVKEY_BUY_PRICE: float(mapping['price_per']),
        CSVKEY_BROKERAGE: brokerage
    }


if __name__ == '__main__':
    convert_xls_to_csv(input_xlsx_file, input_csv_file)
    extracted_data = build_data_store(input_csv_file)
    generate_output_csv(extracted_data)
