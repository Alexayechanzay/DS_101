

import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv("programmingUsed.csv")

# --- ADD THIS LINE TO INVESTIGATE ---
print("Your actual columns are:", data.columns.tolist())

# Comment these out for a quick second so the script doesn't crash
# id = data["Responder_id"]
# lang = data["LanguagesWorkedWith"]
