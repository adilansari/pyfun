import os
from tabula import read_pdf

NOTES_DIR = '$HOME/OneDrive/Documents/Financial/Tax/2020/india/smc_contract_notes'

all_pdf_files = os.listdir(NOTES_DIR)

first_file = os.path.join(NOTES_DIR, all_pdf_files[0])
tables = read_pdf(first_file)

print(tables)

