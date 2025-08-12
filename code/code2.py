# data_module.py

import pandas as pd

def print_csv():
    df = pd.read_csv('code/data.csv')
    df.drop(columns=['Timestamp'], inplace=True)
    pd.set_option('display.max_rows', 1000)
    print(df)


def main_menu():
    while True:
        print("Data Viewer Interface")
        print("1. View dataset")
        print("2. View visualisation")
        print("3. Search or filter data")
        print("4. Exit")
        
        choice = int(input("Select an option (1-6): "))
        if choice == 1:
                print_csv()

            

main_menu()

