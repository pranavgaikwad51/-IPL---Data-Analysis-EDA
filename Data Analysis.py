# Imporitng necessarry libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Loading Dataset
ball_df=pd.read_csv('/content/IPL Ball-by-Ball 2008-2020.csv')
matches_df=pd.read_csv('/content/IPL Matches 2008-2020.csv')

# 1. What was the count of matches played in each season?
matches_df['date'] = pd.to_datetime(matches_df['date'])
matches_df['season'] = matches_df['date'].dt.year
matches_per_season = matches_df['season'].value_counts().sort_index()
# setting the style and figure
sns.set(style='whitegrid')
plt.rcParams['figure.figsize']=(10,6)
# plotting the bargraph
plt.figure()


sns.barplot(x=matches_per_season.index,y=matches_per_season.values,palette='viridis')
plt.xlabel('Season')
plt.ylabel('matches')
plt.title('Matches Per Season')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. How many runs were scored in each season?

merged = ball_df.merge(matches_df[['id','season']],on='id')
run_each_season = merged.groupby('season')['total_runs'].sum()
print(run_each_season)

# 3. What were the runs scored per match in different seasons?

run_per_match =merged.groupby(['season','id'])['total_runs'].sum()
run_per_match

# 4. Who has umpired the most?

umpire=pd.concat([matches_df["umpire1"],matches_df["umpire2"]])
most_common_umpire = umpire.value_counts().idxmax()
most_common_umpire
# 5. Which team has won the most tosses?

most_toss_win=matches_df['toss_winner'].value_counts()
most_toss_win.idxmax()

# 6. What does the team decide after winning the toss?

toss_decision=pd.crosstab(matches_df["toss_winner"],matches_df["toss_decision"])
toss_decision = toss_decision.sum()
toss_decision.idxmax()


# plotting bar graph
plt.figure()
sns.barplot(x=toss_decision.index,y=toss_decision.values,palette='viridis')
plt.title('Decision After Winning Toss')
plt.xlabel('Toss_Decision')
plt.ylabel('Number')
plt.show()

# 7. How does the toss decision vary across seasons?

toss_decision_by_season = matches_df.groupby('season')['toss_decision'].value_counts().unstack()
toss_decision_by_season.plot(kind='bar',stacked=True,colormap='Set2')

# 8. Does winning the toss imply winning the game?
# To calculate Only Percentage 

toss_w = matches_df['toss_winner'] == matches_df['winner']
win_percentage = toss_w.mean()*100
print(f'after toss winning the rate of match win is {win_percentage}')

# Another method 
matches_df['toss_win_match_win'] = matches_df['toss_winner'] == matches_df['winner']
toss_win_match_win_rate = matches_df['toss_win_match_win'].mean()
toss_outcome_counts = matches_df['toss_win_match_win'].value_counts()
# plotting graph
toss_outcome_counts.index = ['Did Not win the Match',"Won MAtch!"]
toss_outcome_counts.plot(kind = "pie",autopct="%1.1f%%",startangle = 45)

# 9. How many times has the chasing team won the match?

chasing_team = (
    ((matches_df['toss_decision'] == 'field') & (matches_df['toss_winner'] == matches_df['winner'])) |
    ((matches_df['toss_decision'] == 'bat') & (matches_df['toss_winner'] != matches_df['winner']))
)

chasing_teams_win_times = chasing_team.sum()
print("Chasing wins:", chasing_teams_win_times)


# 10. Which all teams had won this tournament?
a = matches_df.sort_values('date').groupby('season').tail(1)
team_won_tournament= a[['season','winner']].reset_index(drop=True)
team_won_tournament

# 11. Which team has played the most number of matches?
most_num_matches=pd.concat([matches_df['team1'],matches_df['team2']])
most_num_matches.value_counts().idxmax()

# 12. Which team has won the most number of times?

most_matches_winner=matches_df['winner'].value_counts().idxmax()
most_matches_winner

# 13. Which team has the highest winning percentage?
# count wins per team
wins = matches_df['winner'].value_counts()

# count matches played per team
played = matches_df['team1'].value_counts() + matches_df['team2'].value_counts()

# calculate winning percentage
percentage = (wins / played) * 100

# team with highest win percentage
win_percentage = percentage.idxmax()
print("Team with highest winning %:", win_percentage, percentage.max())


# 14. Is there any lucky venue for a particular team?
matches_df.groupby('winner')['venue'].value_counts().idxmax()

# 15. Innings wise comparison between teams
comparosion_inning_wise = matches_df.groupby(['winner','inning']).size().reset_index(name='wins')
comparosion_inning_wise

16. Which team has scored the most number of 200+ scores?


