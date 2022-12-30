import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from nutil.plot import paperStyle  # (pip install git+https://github.com/anki-xyz/nutil)

download_url = ("https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv")
df = pd.read_csv(download_url)
print(df)
df.sort_values(by=['Median'])
df1 = df.iloc[0:10, :]
# TASK1: Plot the top 10 majors depending on the median earnings of full-time, year-round workers. Make it nice
# looking and prepare the plot for publication. Then save it in a suitable file format to load it into Inkscape.
'''ax = df1.plot(x="Major", y="Median", kind="bar", title="Top 10 majors depending on the median earnings")
ax.set_xticklabels(ax.get_xticklabels(), rotation=10, ha="right")
print(df)
plt.show()
'''
# TASK2: Plot the boxplots of median earnings for the top 5 categories (as measured by median earnings). Then add the
# raw sample points to the plot using a suitable plot type.
df2 = df.iloc[0:21, :]
l = list(df2["Major_category"].unique())
cond1 = df["Major_category"] == l[0]
cond2 = df["Major_category"] == l[1]
cond3 = df["Major_category"] == l[2]
cond4 = df['Major_category'] == l[3]
cond5 = df["Major_category"] == l[4]
df3 = df.where(cond1 | cond2 | cond3 | cond4 | cond5).dropna()
print(df3)
'''ax = sns.boxplot(data=df3, x='Major_category', y='Median')
plt.show()'''
df.sort_values(by=['Unemployment_rate'])
l = list(df["Major_category"].unique())
cond1 = df["Major_category"] == l[0]
cond2 = df["Major_category"] == l[1]
cond3 = df["Major_category"] == l[2]
cond4 = df['Major_category'] == l[3]
cond5 = df["Major_category"] == l[4]
df4 = df.where(cond1 | cond2 | cond3 | cond4 | cond5).dropna()
sns.violinplot(data=df4, x="Major_category", y="Unemployed")
plt.show()
'''
plt.scatter(df["Unemployment_rate"], df['Median'])
plt.plot([0, 0.2], [0, 110000], 'k-')
plt.xlabel("Unemployment Rate")
plt.ylabel("Median Salary")
plt.title("Correlation between Median Salary and Unemployment rate")
plt.show()'''
