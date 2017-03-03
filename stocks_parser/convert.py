import csv
import time

# read the input file into a dict
# parse that dict into a new dict only keeping the needed fields
# dump this new dict into a csv


todays_date = time.strftime("%d/%m/%Y")

conf = (
    ('output/gfinance_formatted_trades.csv', ['Symbol', 'Buy Date', 'Buy Quantity', 'Buy Price']),
    ('output/moneycontrol_formatted_trades.csv', ['BSE/NSE/ISIN Code', 'Buy Date', 'Buy Quantity', 'Buy Price'])
)

def convert(input_file):

    with open(input_file) as input_csv:
        reader = csv.DictReader(input_csv)
        output_data = list(map(_filter_noise, reader))


    for outfile, fieldnames in conf:
        with open(outfile, 'w') as output_csv:
            writer = csv.DictWriter(output_csv, fieldnames=fieldnames, extrasaction='ignore')
            writer.writerows(output_data)

def _filter_noise(row):
    return {
        'BSE/NSE/ISIN Code': row['Symbol '].strip(),
        'Symbol': 'NSE:' + row['Symbol '].strip(),
        'Buy Date': todays_date,
        'Buy Quantity': int(row['Quantity '].strip()),
        'Buy Price': float(row['Price '].strip())
    }

if __name__ == "__main__":
    input_file = "input/sample_input.csv"
    convert(input_file)
