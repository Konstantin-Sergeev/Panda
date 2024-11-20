import pandas as pd
import matplotlib.pyplot as plt


solutions_data = pd.read_html("C:\\Users\Professional\Desktop\plot\\results_ejudge.html")
groups_data = pd.read_excel("C:\\Users\Professional\Desktop\plot\students_info.xlsx")

list_length = int(groups_data["login"].count())

print(list_length)

for i in range(list_length):
    log = groups_data.iloc[i]["login"]

    tmp = solutions_data[0].loc[solutions_data[0]["User"] == log]
    tmp1 = tmp["Solved"]
    tmp2 = int(tmp1.iloc[0])
    groups_data.loc[i, "solved"] = tmp2
#groups_data = groups_data.iloc[1:,1:4]
group_faculty = groups_data.groupby(["group_faculty"])["solved"].mean()
group_out = groups_data.groupby("group_out")["solved"].mean()
print(group_faculty.head(8))
print(group_out.head(8))
fig, ax = plt.subplots(figsize = (10, 8))
plt.title("А)")
print(groups_data)
group_faculty.plot(kind = "bar", label = "Среднее решенное в группе количество задач")
ax.grid()

ax.set_ylim(0, 2.5)
plt.xlabel('Group_faculty')
plt.ylabel('Solved problems')
plt.legend()
plt.show()
fig, ax = plt.subplots(figsize = (10, 8))
plt.title("Б)")
group_out.plot(kind = "bar", label = "Среднее решенное в группе по информатике количество задач")
ax.grid()


ax.set_ylim(0, 6)
plt.xlabel('group_out')
plt.ylabel('Solved problems')
plt.legend()
plt.show()
