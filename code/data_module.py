# data_module.py
import pandas as pd
import time
import matplotlib.pyplot as plt

# all my functions for the main code!!

def data_updated():
    #load dataset from the csv file
    df = pd.read_csv(
         'code/data.csv',
         on_bad_lines='skip', #skips broken or 'bad' lines
         header = None, #not treat the first row of data as column names
         names = ["Timestamp", #uses these as column names instead
                "| Play lootbox games |",
                "| Spent money on lootbox systems |",
                "| Spending feelings (1-bad, 5-great) |"]
         )
    df.drop(columns=['Timestamp'], inplace=True) #removes the timestamp column
    df.dropna(inplace = True) #removes rows that have NA (no answer)
    substring = 'yes, no' #removes rows that have 'yes, no' as an answer 
    filter = df['| Play lootbox games |'].str.contains(substring)
    df = df[~filter]
    pd.set_option('display.max_rows', 1000) #makes sures to diplay all my data
    return df #so i can use the data later in my program

def view_dataset():
        df = data_updated()
        print(df)

def data_filtering ():
        df = data_updated()

        while True:
                time.sleep(1)
                filter_choice = input("""
\nFilter from:
1. Whether students play lootbox games 
2. Whether students spent money on lootbox games 
3. How students feel about spending money on lootbox systems (1-bad, 5-great) 
4. Exit 
Select an option (1-4): """)
        
                if filter_choice == '1':
                        time.sleep (1) 
                        print(df.loc[:,["| Play lootbox games |"]])
                        values = df.loc[:,["| Play lootbox games |"]]
                        
                        print(df["| Play lootbox games |"].value_counts()) #counts the amount of different values

                elif filter_choice == '2': 
                        time.sleep (1) 
                        print(df.loc[:,["| Spent money on lootbox systems |"]])
                        print(df["| Spent money on lootbox systems |"].value_counts()) 

                elif filter_choice == '3': 
                        time.sleep (1) 
                        print(df.loc[:,["| Spending feelings (1-bad, 5-great) |"]]) 
                        print(df["| Spending feelings (1-bad, 5-great) |"].value_counts())

                elif filter_choice == '4': 
                        return #exit filter menu
                
                else: 
                        print("\nInvalid selection. Please choose a number between 1 and 4.")

def data_visualisation():
    while True:
        time.sleep(1)
        visualisation_choice = input("""

View visualisation of: 
1. Gacha game players vs spenders
2. Comparison of spending feelings (1-bad, 5-great)
3. Exit

Select an option (1-3):
""")

        if visualisation_choice == '1':
                plt.clf() #clears previous visualisation window
                categories = ['gacha game players', 'gacha game spenders ']
                values = [75/155 * 100, 52/155 * 100] #converted to percentage

                plt.bar(categories, values, color= ['skyblue', 'orange'])
                plt.title('Gacha game players vs spenders')
                plt.ylabel('percentage of total students (%)')

                plt.show(block= False) #so you can still run the code without having exited the visualisation window

        elif visualisation_choice == '2': 
                plt.clf()
                categories = ['1', '2', '3', '4', '5']
                values = [70, 36, 16, 8, 25]

                plt.bar(categories, values, color= ['skyblue', 'orange', 'yellow', 'blue', '#FC6238']) #colours
                plt.title('Comparison of spending feelings (1-bad, 5-great)')
                plt.ylabel('Number of students chosen option')

                plt.show(block= False)

        elif visualisation_choice == '3': 
                return 
                
        else: 
                print("\nInvalid selection. Please choose a number between 1 and 3.")
