import pandas as pd

buy_list = pd.read_csv("C:\\Users\Professional\Downloads\\transactions.csv")
OK_0 = buy_list[buy_list["STATUS"] == "OK"]

first_transaction = OK_0["SUM"].max()
OK_1 = OK_0.sort_values(by = "SUM",ascending = False)
OK_2 = OK_0[OK_0["CONTRACTOR"] == "Umbrella, Inc"]
SUM = OK_2["SUM"].sum()
DATA = OK_1["SUM"]
print("Here are 3 biggest transactions with status 'OK'")
print(DATA.head(3))
print("And sum of all of the transactions to Umbrella, Inc")
print(SUM)






