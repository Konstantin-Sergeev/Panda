import pandas as pd

solutions_data = pd.read_html("C:\\Users\Professional\Desktop\plot\\results_ejudge.html")[0]
groups_data = pd.read_excel("C:\\Users\Professional\Desktop\plot\students_info.xlsx")

list_length = int(groups_data["login"].count())

solutions_data = solutions_data[(solutions_data["G"] >= 20) | (solutions_data["H"] >= 20)]
for i in range(solutions_data["User"].count()):
    log = solutions_data.iloc[i]["User"]
    for j in range(list_length):
        if groups_data.iloc[j]["login"] == log:
            groups_data.loc[j, "Bool"] = True

groups_data = groups_data[groups_data["Bool"] == True]
answer = groups_data.groupby(["group_faculty", "group_out"]).value_counts()
print(answer.head(20))