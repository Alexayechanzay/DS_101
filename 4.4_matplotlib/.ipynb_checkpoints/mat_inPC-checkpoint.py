import  matplotlib.pyplot as plt
import random

from matplotlib import colors
from matplotlib.lines import lineStyles

month = [_ for _ in range(1,13,1)]
# income_job1 = [ random.randint(1500000,10000000) for _ in range(12)]
# income_job2 = [ random.randint(100000,5000000) for _ in range(12)]

income1 = [2767794, 2417862, 5931018, 3032457, 6908473, 5043668, 5942713, 3676690, 2691705, 1897640, 1905948, 1632472]
income2 = [185831, 4136857, 1187333, 1151318, 3700236, 3786138, 1222778, 3321447, 1672130, 2233046, 1813440, 1216910]

# plotting
plt.plot(month, income1,color="red",linestyle="dashed",label="JOB1")
plt.plot(month, income2,color="blue",label="JOB2")
plt.plot(month, income2)
plt.xlabel("Month")
plt.ylabel("Income  ($)")
plt.title("Monthly Income of two jobs in 2026")
plt.show()