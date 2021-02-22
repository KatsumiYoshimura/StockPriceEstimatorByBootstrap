# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
#      問題設定:
# 

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %%
# 期間
# steps日の株価変動を評価する
day_per_month = 20
steps = 60*day_per_month


# %%
# sample_number個の時系列データを生成し、株価の評価をする
sample_number = 100000


# %%
# 株価の日次時系列データ
pd_data_1 = pd.read_csv('sample_data_1.csv',header=None)
raw_data_1= np.array(pd_data_1[0])

log_data_1 = np.log(raw_data_1)
# 日次収益率
sample_rate_1= log_data_1[1:len(log_data_1)]-log_data_1[0:len(log_data_1)-1]

# 配当
# 12*day_per_month毎に受け取る
dividend_1 = 50


# %%
# 株価
price_1 = np.ones(sample_number)*raw_data_1[len(raw_data_1)-1]
# 累積配当受取額
cash = 0
# sample_number個の株価データの平均値
price_1_avg = [price_1[0]]
total_1_avg = [price_1[0]+cash]
# sample_number個の株価データの中間値
price_1_half = [price_1[0]]
total_1_half = [price_1[0]+cash]
# Value At Risk - 99%の確率で、株価はこれより高くなる
price_1_var = [price_1[0]]
total_1_var = [price_1[0]+cash]
# Average + 1 sigma相当 - 35%の確率で、株価はこれより高くなる
price_1_p = [price_1[0]]
total_1_p = [price_1[0]+cash]
# Average - 1 sigma相当 - 65%の確率で、株価はこれより高くなる
price_1_n = [price_1[0]]
total_1_n = [price_1[0]+cash]

t = [len(raw_data_1)-1]
for i in range(1,steps+1):
    t.append(len(raw_data_1)+i)
    # 変動率をサンプリング
    index = np.random.randint(0,len(sample_rate_1),sample_number)
    price_1 = (1+sample_rate_1[index])*price_1

    # 配当
    if i % (12*day_per_month) == 0:
        cash = cash + dividend_1

    price_1.sort()
    # sample_number個の株価データの平均値
    price_1_avg.append(np.average(price_1))
    total_1_avg.append(np.average(price_1)+cash)
    # sample_number個の株価データの中間値
    price_1_half.append(price_1[int(0.5*sample_number)])
    total_1_half.append(price_1[int(0.5*sample_number)]+cash)
    # Value At Risk - 99%の確率で、株価はこれより高くなる
    price_1_var.append(price_1[int(0.01*sample_number)])
    total_1_var.append(price_1[int(0.01*sample_number)]+cash)
    # Average + 1 sigma相当 - 35%の確率で、株価はこれより高くなる
    price_1_n.append(price_1[int(0.35*sample_number)])
    total_1_n.append(price_1[int(0.35*sample_number)]+cash)
    # Average - 1 sigma相当 - 65%の確率で、株価はこれより高くなる
    price_1_p.append(price_1[int(0.65*sample_number)])
    total_1_p.append(price_1[int(0.65*sample_number)]+cash)


# %%
plt.plot(raw_data_1 , label="raw data")
plt.plot(t, price_1_avg , label="Average")
plt.plot(t, price_1_half , label= "Half")
plt.plot(t, price_1_var , label= "Value At Risk")
plt.plot(t, price_1_p , label="+1 sigma")
plt.plot(t, price_1_n , label="-1 Sigma")
plt.legend()
plt.show()


# %%
plt.plot(raw_data_1 , label="raw data")
plt.plot(t, total_1_avg , label="Average")
plt.plot(t, total_1_half , label= "Half")
plt.plot(t, total_1_var , label= "Value At Risk")
plt.plot(t, total_1_p , label="+1 sigma")
plt.plot(t, total_1_n , label="-1 Sigma")
plt.legend()
plt.show()


