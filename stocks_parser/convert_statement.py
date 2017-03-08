import os

input_csv_file = 'input/profit_loss_statement.csv'
input_xlsx_file = 'input/profit_loss_statement.xlsx'


def convert_xls_to_csv(xlsfile, csvfile):
    os.system('in2csv {} > {}'.format(xlsfile, csvfile))


if __name__ == '__main__':
    convert_xls_to_csv(input_xlsx_file, input_csv_file)