import wehoop
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
%matplotlib notebook

#load data sample
df = wehoop.wbb.load_wbb_player_boxscore(seasons=range(2020,2021))

df['ft-successful'] = df['ft'].apply(lambda x: 
                                  pd.to_numeric(x.split('-')[0]))

df['ft-attempted'] = df['ft'].apply(lambda x: 
                                  pd.to_numeric(x.split('-')[1]))

keys=['athlete_display_name']
df1 = df.groupby(keys)['ft-successful']
df2 = df.groupby(keys)['ft-attempted']

player='Chelsey Perry' #random player name
ft_s = df1.get_group(player).values
ft_a = df2.get_group(player).values

#plot cumulative distribution function
x1 = np.sort(ft_s)
x2 = np.sort(ft_a)
y = np.arange(len(ft_a))/ float(len(ft_a))
plt.xlabel('Free Throws')
plt.ylabel('CDF')
plt.grid()
plt.plot(x1, y,c='g',linewidth = '3')
plt.plot(x2, y,c='r',linewidth = '3')
