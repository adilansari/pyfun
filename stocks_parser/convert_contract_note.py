import os
import csv
import re
import xlsxwriter
from config import *
from datetime import datetime

input_csv_file = 'input/contract_note.csv'
input_xlsx_file = 'input/profit_loss_statement.xls'

STOCK_NAMES = STOCK_SYMBOLS.keys()
DATE_REGEX = r'[0-2][0-9]\/[0-1][0-9]\/20[1-2][0-9]'

# TODO: Value research date format, value research xls, cross verify with unit count

def convert_xls_to_csv(xlsfile, csvfile):
    os.system('ssconvert {} {}'.format(xlsfile, csvfile))


def convert_csv_to_xls(csvfile):
    wb = xlsxwriter.Workbook(csvfile.replace('.csv', '.xls'))
    ws = wb.add_worksheet("WS1")
    with open(csvfile, 'r') as input_csv:
        table = csv.reader(input_csv)
        i = 0
        for row in table:
            ws.write_row(i, 0, row)
            i += 1
    wb.close()


def build_data_store(csvfile):
    data_store = []
    trade_date = ''

    with open(csvfile, 'r') as lines:
        for line in lines:
            if 'Trade Date' in line:
                trade_date = _extract_date(line)
                continue

            stock_symbol = _extract_stock_symbol(line)
            if not stock_symbol:
                continue
            purchase_data = _extract_stock_info(stock_symbol, line)
            if not purchase_data:
                continue
            purchase_data['date'] = trade_date
            data_store.append(purchase_data)
    return data_store


def _extract_stock_info(stock_symbol, line):
    temp_buffer = dict()
    array = line.split(',')
    temp_buffer['symbol'] = stock_symbol
    buy_index = array.index('Buy')
    temp_buffer['qty'] = int(array[buy_index + 1])
    if not temp_buffer['qty']:
        return None
    temp_buffer['price_per'] = float(array[buy_index + 3])
    temp_buffer['charges'] = float(array[buy_index + 4]) * temp_buffer['qty']
    temp_buffer['stt'] = 0
    return temp_buffer


def _extract_date(line):
    try:
        date_string = re.findall(DATE_REGEX, line)[0]
        return datetime.strptime(date_string, "%d/%m/%Y")
    except ValueError:
        return None


def _extract_stock_symbol(line):
    for name, symbol in STOCK_SYMBOLS.items():
        if name in line:
            return symbol
    return None


def generate_output_csv(filtered_data):
    csv_buffer = list(map(_create_struct, filtered_data))

    # display total quantity and amount
    print('Total quantity: ', sum(entry[CSVKEY_BUY_QTY] for entry in csv_buffer))
    print('Total brokerage: ', sum(entry[CSVKEY_BROKERAGE] for entry in csv_buffer))
    print('Total Amount: ', sum(entry[CSVKEY_AMOUNT] for entry in csv_buffer))
    print('Total transactions: ', len(filtered_data))

    for key in [MONEYCONTROL, VALUE_RESEARCH]:
        conf = CONFIG[key]
        with open(conf[OUTPUT_FILE], 'w') as output_csv:
            writer = csv.DictWriter(output_csv, fieldnames=conf[FIELDNAMES], extrasaction='ignore')
            writer.writeheader()
            writer.writerows(csv_buffer)

        # convert output_csv to xls ... nothing much
        if key == VALUE_RESEARCH:
            convert_csv_to_xls(conf[OUTPUT_FILE])


def _create_struct(mapping):
    stock_symbol = mapping['symbol']
    brokerage = float('{0:.2f}'.format(float(mapping['charges']) + float(mapping['stt'])))
    qty = int(mapping['qty'])
    price_per = float(mapping['price_per'])
    return {
        CSVKEY_ISIN_CODE: stock_symbol,
        CSVKEY_SYMBOL: stock_symbol,
        CSVKEY_BUY_DATE: mapping['date'].strftime(CONFIG[MONEYCONTROL][DATE_FORMAT]),
        # CSVKEY_PURCHASE_DATE: mapping['date'].strftime(CONFIG[GOOGLE_FINANCE][DATE_FORMAT]),
        CSVKEY_DATE: mapping['date'].strftime(CONFIG[VALUE_RESEARCH][DATE_FORMAT]),
        CSVKEY_BUY_QTY: qty,
        CSVKEY_UNITS: qty,
        CSVKEY_BUY_PRICE: price_per,
        CSVKEY_BROKERAGE: brokerage,
        CSVKEY_TRANSACTION_TYPE: 'Purchase',
        CSVKEY_TOTAL_AMOUNT: float("{0:.2f}".format(qty * price_per)),
        CSVKEY_AMOUNT: float("{0:.2f}".format(qty * price_per))
    }


if __name__ == '__main__':
    extracted_data = build_data_store(input_csv_file)
    generate_output_csv(extracted_data)
