#data_module.py

import pandas as pd
import matplotlib.pyplot as plt
import time

from data_module import data_filtering, view_dataset

def main_menu():
    while True:
        time.sleep (1)
        print("""\n
 -------------------------
|Data Viewer Interface:   |
|                         |
|1. View dataset          |
|2. View visualisation    |
|3. Filter data           |
|4. Exit                  | 
 -------------------------              
""")
        choice = int(input("""
----------------------
Select an option (1-4): """))

        if choice == 1:
                time.sleep (1)
                print("\nWhether students at Gosford High School:\n")
                view_dataset()
        elif choice == 2:
                print("yay")
        elif choice == 3:
                data_filtering()
        elif choice == 4:
                time.sleep (1)
                print("\nExiting program!!\n")
                break
        else:
                print("Invalid selection. Please choose a number between 1 and 4.")
        
print("\nLoading...")
main_menu()



