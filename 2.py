import pandas as pd
import matplotlib.pyplot as plt

flights = pd.read_csv("C:\\Users\Professional\Downloads\\flights.csv")

all_flights = flights["CARGO"].count()

all_cost = flights["PRICE"].sum()
all_weight = flights["WEIGHT"].sum()

flights_num = flights["CARGO"].value_counts()
flights_num1 = flights["CARGO"].value_counts()/all_flights*100
print(flights_num.head())

flights_cost = flights.groupby("CARGO")["PRICE"].sum()
flights_cost1 = flights.groupby("CARGO")["PRICE"].sum()/all_cost*100
print(flights_cost.head())
flihts_weight = flights.groupby("CARGO")["WEIGHT"].sum()
flihts_weight1 = flights.groupby("CARGO")["WEIGHT"].sum()/all_weight*100
print(flihts_weight.head())

fig, ax = plt.subplots(figsize = (10, 8))

flights_num1.plot.bar(color = "r", label = "Part of summary flights | %d total" %(all_flights))
flights_cost1.plot.bar(color = "g", label = "Part of summary cost | %d$ total" %(all_cost))
flihts_weight1.plot.bar( color = "b", label = "Part of all transported weight | %dкг total" %(all_weight))
plt.ylabel("% of all")
ax.grid()
ax.set_ylim(0, 100)
plt.legend()
plt.show()