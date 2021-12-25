import wehoop
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
%matplotlib notebook

# Data Preparation.
df = wehoop.wbb.load_wbb_player_boxscore(seasons=range(2020,2021))
keys=['team_short_display_name','game_id']
unique_athletes_by_team = df.groupby(keys)['athlete_id'].agg('count')

#CDF of Unique Players
#For a Specific Team
data = ft_success_by_team.get('Northern Iowa').values
x = np.sort(data)
y = np.arange(len(data)) / float(len(data))
plt.xlabel('Unique Players')
plt.ylabel('CDF')
plt.title('Northern Iowa')
plt.grid()
plt.plot(x, y,c='g',linewidth = '3')

#For a collection of teams
def subplot(team,i,j,xlabel,ylabel):
    data = ft_success_by_team.get(team).values
    x = np.sort(data)
    y = np.arange(len(data)) / float(len(data))
    axis[i,j].set_xlabel(xlabel)
    axis[i,j].set_ylabel(ylabel)
    axis[i,j].plot(x, y,c='g',linewidth = '3')
    axis[i,j].set_title(team)
    axis[i,j].grid()
    
figure, axis = plt.subplots(2, 2)
subplot('Northern Iowa',0,0,'','CDF')
subplot('Abil Christian',0,1,'','')
subplot('Villanova',1,0,'Unique Players','CDF')
subplot('Charlotte',1,1,'UniquePlayers','')

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

plt.show()
