import os

input_csv_file = 'input/profit_loss_statement.csv'
input_xlsx_file = 'input/profit_loss_statement.xlsx'


def convert_xls_to_csv(xlsfile, csvfile):
    os.system('in2csv {} > {}'.format(xlsfile, csvfile))

def build_data_store(csvfile):
    clean_buffer = _clean_csv(csvfile)
    print clean_buffer

    # convert this buffer to a dict
    # extract data from this buffer
    # create both output files

def _clean_csv(csvfile):
    def _is_useful_data(line):
        if 'Gain' in line and 'Charges' in line:
            return True
        # if a key from symbol map exists here
        # return True
        return False

    with open(csvfile, 'r') as lines:
        return filter(_is_useful_data, lines)

if __name__ == '__main__':
    convert_xls_to_csv(input_xlsx_file, input_csv_file)
    build_data_store(input_csv_file)

# build a name => Symbol map iin conf.py