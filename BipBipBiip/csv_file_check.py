import math
import csv
import sys

def load_data(file_name='phonebook.csv'):
    with open(file_name, 'r') as data_file:
        reader = csv.reader(data_file, delimiter=',')
        return list(reader)[1:]

def is_valid_phone_number(phone_number:str):
    num_digits = 0

    for char in phone_number:
        if char not in "0123456789-+ ().":
            return False
    for i in phone_number:
        if i in "0123456789":
            num_digits += 1
            continue
    if num_digits < 10:
        return False
    return True
    
convert_from_hex = lambda x: bytes.fromhex(x).decode('utf-8')

if __name__ == "__main__":
    flag = ""
    data = load_data()
    for line, count in zip(data, range(1, len(data) + 1)):
        if not is_valid_phone_number(line[4]):
            print(f"\t{count} - Weird Number : {line[4]}.")
            try: 
                print(f"\tMessage : {convert_from_hex(line[4])}")
                flag += convert_from_hex(line[4])
            except:
                continue
    print(f"Flag : {flag}")
    