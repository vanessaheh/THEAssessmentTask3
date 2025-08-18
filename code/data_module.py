# data_module.py
import pandas as pd
import time
import matplotlib.pyplot as plt

def data_updated():
    df = pd.read_csv(
         'code/data.csv',
         on_bad_lines='skip',
         header = None,
         names = ["Timestamp",
                "| Play lootbox games |",
                "| Spent money on lootbox systems |",
                "| Spending feelings (1-bad, 5-great) |"]
         )
    df.drop(columns=['Timestamp'], inplace=True)
    df.dropna(inplace = True)
    substring = 'yes, no'
    filter = df['| Play lootbox games |'].str.contains(substring)
    df = df[~filter]
    pd.set_option('display.max_rows', 1000)
    return df

def view_dataset():
        df = data_updated()
        print(df)

def data_filtering ():
        df = data_updated()

        while True:
                time.sleep(1)
                filter_choice = int(input("""
\nFilter from:
1. Whether students play lootbox games 
2. Whether students spent money on lootbox games 
3. How students feel about spending money on lootbox systems (1-bad, 5-great) 
4. Exit 
Select an option (1-4): """)) 
        
                if filter_choice == 1:
                        time.sleep (1) 
                        print(df.loc[:,["| Play lootbox games |"]])
                        values = df.loc[:,["| Play lootbox games |"]]
                        
                        print(df["| Play lootbox games |"].value_counts())

                elif filter_choice == 2: 
                        time.sleep (1) 
                        print(df.loc[:,["| Spent money on lootbox systems |"]])
                        print(df["| Spent money on lootbox systems |"].value_counts()) 

                elif filter_choice == 3: 
                        time.sleep (1) 
                        print(df.loc[:,["| Spending feelings (1-bad, 5-great) |"]]) 
                        print(df["| Spending feelings (1-bad, 5-great) |"].value_counts())

                elif filter_choice == 4: 
                        return 
                
                else: 
                        print("\nInvalid selection. Please choose a number between 1 and 4.")

def data_visualisation():
    while True:
        time.sleep(1)
        visualisation_choice = int(input("""

View visualisation of: 
1. Gacha game players vs spenders
2. Comparison of spending feelings (1-bad, 5-great)
3. Exit
"""))

        if visualisation_choice == 1:
                plt.clf()
                categories = ['gacha game players', 'gacha game spenders ']
                values = [73/153 * 100, 53/153 * 100]

                plt.bar(categories, values, color= ['skyblue', 'orange'])
                plt.title('Gacha game players vs spenders')
                plt.ylabel('percentage of total students (%)')

                plt.show(block= False)

        elif visualisation_choice == 2: 
                plt.clf()
                categories = ['1', '2', '3', '4', '5']
                values = [70, 36, 16, 8, 25]

                plt.bar(categories, values, color= ['skyblue', 'orange', 'yellow', 'blue', '#FC6238'])
                plt.title('Comparison of spending feelings (1-bad, 5-great)')
                plt.ylabel('Number of students chosen option')

                plt.show(block= False)

        elif visualisation_choice == 3: 
                return 
                
        else: 
                print("\nInvalid selection. Please choose a number between 1 and 4.")
