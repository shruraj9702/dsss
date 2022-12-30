import collections

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/census_income_dataset.csv')
data["AGE"].plot.hist(bins=50)
plt.xlabel("Age")
plt.title("Age distribution of Participants")
plt.show()
data["RELATIONSHIP"].value_counts().plot(kind='bar', title="How oft does each relationship status occur?",
                                         legend=False)
plt.show()
data["RELATIONSHIP"].value_counts().plot(kind='pie', title="How often does each relationship status occur?",
                                         legend=False, autopct='%1.1f%%')
plt.show()

plt.scatter(data["AGE"], data['HOURS-PER-WEEK'])
plt.plot([0, 100], [0, 100], 'k-')
plt.xlabel("Age")
plt.ylabel("Work Hours per week")
plt.title("Correlation between Age and work hours per week")
plt.show()

new_dict = dict(zip(data["AGE"], data['HOURS-PER-WEEK']))

od = collections.OrderedDict(sorted(new_dict.items()))

X = np.arange(20, 100, 10)
df1 = {}
lst = []
for i, x in enumerate(X):
    df1[str(x)] = np.where((x > list(od.keys())))

new_list = list(df1.values())

for i, x in enumerate(list(df1.values())):
    if i > 0:
        new_list[i] = np.setdiff1d(x, new_list[i - 1])
print(new_list)
# print(list(data["salary_condition"].value_counts().to_dict().values()))


# data["EDUCATION"].value_counts()[0:len(data["EDUCATION"])].plot(x="Education", y="Frequency",kind='bar')
new_dict = dict(zip(data["EDUCATION"], data["EDUCATION-NUM"]))
data['salary_condition'] = data['SALARY'].apply(lambda x: True if x == ' >50K' else False)
# data["SALARY"]
# data["EDUCATION"]
# data["EDUCATION-NUM"]
X_axis = np.arange(len(new_dict.keys()))
df1 = {}
for x in new_dict.keys():
    df1[str(x)] = len(data[(data.EDUCATION == x) & (data.SALARY != ' >50K')])
print(df1)
df2 = {}
for x in new_dict.keys():
    df2[str(x)] = len(data[(data.EDUCATION == x) & (data.SALARY != ' <=50K')])
print(df2)
df3 = {}
for x in new_dict.keys():
    df3[str(x)] = len(data[(data.EDUCATION == x)])
print(df3)

lst1 = list(df1.values())
lst2 = list(df2.values())

plt.bar(X_axis - 0.2, lst1, 0.4, label='> 50k')
plt.bar(X_axis + 0.2, lst2, 0.4, label='<= 50k')
plt.xticks(X_axis, list(new_dict.keys()))
plt.xlabel("Education level")
plt.ylabel("Number of participants")
plt.title("Salary vs Education")
plt.legend()
plt.show()
