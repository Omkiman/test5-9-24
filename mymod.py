import os


# exit protocol
def exitprog():
    print("Exiting program...")
    exit()

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# display menu
def menu(actions):
    for i in actions:
        print(f"{i.value} - {i.name}")
    return (int(input("your selection? ")))

def countCuts(df):
    allCuts = df['cut'].unique() # finds only unique cuts listed and adds them to a list
    for i in allCuts:
        print(i)
    selection = input("which cut would you like to count? ")
    if selection in allCuts: 
        countCut = (df['cut'] == selection).sum() # sums up the rows with the specified cut in them
        print (f"there are {countCut} diamonds of the {selection} cut.")
    else:
        print("invalid choice")

def medianOfCuts(df):
    allCuts = df['cut'].unique() # finds only unique cuts listed and adds them to a list
    for i in allCuts:
        print(i)
    selection = input("which cut would you like to find the median of? ")
    if selection in allCuts:
        cutDf = df[df['cut'] == selection] # makes a separate DF only containing rows with the specified cut
        medianCut = cutDf['price'].median() # finds the median of price column in the new DF
        print (f"the median price of the {selection} cut is {medianCut}")
    else:
        print("invalid choice")

def caratMeanByCut(df):
    allCuts = df['cut'].unique() # finds only unique cuts listed and adds them to a list
    for i in allCuts:
        cutDf = df[df['cut'] == i] # makes a separate DF only containing rows with the specified cut
        caratMean = cutDf['carat'].mean() # finds the mean of carat column in the new DF
        print(f"{i} - average carat is {round(caratMean, 3)} carat.")
    print("rounded to 3 deciman places")

def priceMeanByColor(df):
    allCuts = df['color'].unique() # finds only unique cuts listed and adds them to a list
    for i in allCuts:
        cutDf = df[df['color'] == i] # makes a separate DF only containing rows with the specified color
        priceMean = cutDf['price'].mean() # finds the mean of price column in the new DF
        print(f"{i} - average price is {round(priceMean)}.")
    print("rounded")


