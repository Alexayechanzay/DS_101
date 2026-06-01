import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
from numpy.polynomial import laguerre

plt.style.use("fivethirtyeight")

lang_counter = Counter()

# Transfer .csv data to data Obj
data = pd.read_csv("programmingUsed.csv")
id = data["Responder_id"]
lang = data["LanguagesWorkedWith"]

# Data cleaning
for response in lang:
    # count the number of each prog_lang used
    lang_counter.update(response.split(';'))

print(lang_counter)

# Extract data
languages =[]
user_count = []

# output the 10 most common used prog_lang
for i in lang_counter.most_common(20):
    languages.append(i[0]) # x-axis
    user_count.append(i[1]) # y-axis

print(languages)
print(user_count)


languages.reverse()
user_count.reverse()

# visualization
plt.barh(languages, user_count) # barh = horizontal bar

plt.title("10 Most preferred Languages")
plt.xlabel("Number of users")
plt.ylabel("Programming Languages")
plt.tight_layout() # to enable x,y and etc to be fit into the window

plt.show()

