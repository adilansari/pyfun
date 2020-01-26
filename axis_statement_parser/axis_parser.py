import csv

"""
- read the normal file
- subset of lines from '01-01-2019' to '31-12-2019'
"""

FILE_NAMES = ['nre.csv', 'nro.csv', 'nro_pis.csv']
TRXN_DETAILS_KEY = 'PARTICULARS'
CREDIT_KEY = 'CR'
DEBIT_KEY = 'DR'
INTEREST_KEY = 'Int.Pd'
TAX_KEY = 'WTax.Pd'

for file_name in FILE_NAMES:
    interest_earned = []
    tax_deducted = []
    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            transaction_details = row.get(TRXN_DETAILS_KEY)
            if INTEREST_KEY in transaction_details:
                interest_earned.append(float(row.get(CREDIT_KEY).strip()))
            if TAX_KEY in transaction_details:
                tax_deducted.append(float(row.get(DEBIT_KEY).strip()))

    total_interest, total_tax = sum(interest_earned), sum(tax_deducted)
    print '\naccount: {}, int_vals: {}, tax_vals: {}, total_interest: {}, total_tax: {}\n'.format(
        file_name.split('.')[0],
        len(interest_earned),
        len(tax_deducted),
        total_interest,
        total_tax
    )