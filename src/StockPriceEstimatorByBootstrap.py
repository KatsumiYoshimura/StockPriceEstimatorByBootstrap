# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
#    問題設定:
# 

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %%
# 期間
# steps日の株価変動を評価する
day_per_month = 20
steps = 24*day_per_month


# %%
pd_data = pd.read_csv('sample_data.csv',header=None)
raw_data= np.array(pd_data[0])

log_data = np.log(raw_data)
# 日次収益率
sample_rate= log_data[1:len(log_data)]-log_data[0:len(log_data)-1]


# %%
sample_number = 100000

price = np.ones(sample_number)*raw_data[len(raw_data)-1]

x_avg = [price[0]]
x_var = [price[0]]
x_half = [price[0]]
x_p = [price[0]]
x_n = [price[0]]

t = [len(raw_data)-1]
for i in range(0,steps):
    t.append(len(raw_data)+i)
    index = np.random.randint(0,len(sample_rate),sample_number)
    price = (1+sample_rate[index])*price

    price.sort()
    x_avg.append(np.average(price))
    x_var.append(price[int(0.01*sample_number)])
    x_half.append(price[int(0.5*sample_number)])
    x_n.append(price[int(0.35*sample_number)])
    x_p.append(price[int(0.65*sample_number)])

plt.plot(raw_data)
plt.plot(t, x_avg)
plt.plot(t, x_half)
plt.plot(t, x_var)
plt.plot(t, x_p)
plt.plot(t, x_n)
plt.show()


# %%



