#data_module.py

#imported libraries
import pandas as pd
import matplotlib.pyplot as plt
import time

#Importing my functions for data_module.py
from data_module import data_filtering, view_dataset, data_visualisation

#main menu as a function
def main_menu():
    while True: #plays this as the main menu until the user chooses to exit
        time.sleep (1) # Pause for one second before showing menu
        
        #user interface
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
        #the number they choose goes through an if elif else statement to display different outcomes
        choice = int(input("""
----------------------
Select an option (1-4): """))

        if choice == 1:
                time.sleep (1)
                print("\nWhether students at Gosford High School:\n")
                view_dataset() #my functions
        elif choice == 2:
                data_visualisation()
        elif choice == 3:
                data_filtering()
        elif choice == 4:
                time.sleep (1)
                print("\nExiting program!!\n")
                break #exit the loop and end program
        else: #handle invalid input
                print("Invalid selection. Please choose a number between 1 and 4.")
        
#loading message and launch the main menu
print("\nLoading...")
main_menu()



