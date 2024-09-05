import pandas as pd 
from enum import Enum
import mymod as my


# menu items
class actions(Enum):
    VIEW = 1
    STATS = 2
    CLEAR = 3
    EXIT = 4

# statistics menu
class Stats(Enum):
    MostExpensive = 1
    MeanPrice = 2
    CountByCut = 3
    CountColors = 4
    PriceMedianByCut = 5
    CaratMeanByCut = 6
    PriceMeanByColor = 7
    RETURN = 8

#entry point
if __name__ == "__main__":

    # load our CSV
    try:
        df = pd.read_csv('diamonds.csv')
    except:
        print("Error: Unable to load CSV file.")

    #main menu
    while True:
        selection = my.menu(actions)
        if selection == actions.EXIT.value:
            my.exitprog()
        elif selection == actions.VIEW.value:
            print(df)
        elif selection == actions.CLEAR.value:
            my.clear()
        elif selection == actions.STATS.value:
            while True:
                selection = my.menu(Stats)
                if selection == Stats.RETURN.value:
                    break
                elif selection == Stats.MostExpensive.value:
                    mostExpensive = df.loc[df['price'].idxmax()] #Finds the most expensive item rowID, then pulls the entire row
                    print(f"The most expensive diamond costs {mostExpensive['price']}, here are the full details: \n{mostExpensive}")
                elif selection == Stats.MeanPrice.value:
                    print(f"The average price for a diamond is: {round(df['price'].mean())} (rounded)")
                elif selection == Stats.CountByCut.value:
                    my.countCuts(df)
                elif selection == Stats.CountColors.value:
                    colors = df['color'].unique() # finds only unique colors listed and adds them to a list
                    print(f"there are {len(colors)} listed colors, the colors are {colors} \n(I don't get it either, something to do with color quality)")
                elif selection == Stats.PriceMedianByCut.value:
                    my.medianOfCuts(df)
                elif selection == Stats.CaratMeanByCut.value:
                    my.caratMeanByCut(df)
                elif selection == Stats.PriceMeanByColor.value:
                    my.priceMeanByColor(df)
                else:
                    print("invalid choice")
        else:
            print("invalid choice")
