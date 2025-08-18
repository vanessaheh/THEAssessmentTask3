# data_module.py
import pandas as pd
import time
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
                        print("\n", df.loc[:,["| Play lootbox games |"]])
                        values = df.loc[:,["| Play lootbox games |"]]

                elif filter_choice == 2: 
                        time.sleep (1) 
                        print("\n", df.loc[:,["| Spent money on lootbox systems |"]]) 

                elif filter_choice == 3: 
                        time.sleep (1) 
                        print("\n", df.loc[:,["| Spending feelings (1-bad, 5-great) |"]]) 
                
                elif filter_choice == 4: 
                        return 
                
                else: 
                        print("\nInvalid selection. Please choose a number between 1 and 4.")

