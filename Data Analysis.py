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

# 16. Which team has scored the most number of 200+ scores?

df = ball_df.groupby(['id','batting_team'])['total_runs'].sum().reset_index()
totals = df[df['total_runs']>=200]
team_run_more_than_200 = totals.groupby('batting_team')['total_runs'].value_counts()
print(team_run_more_than_200.idxmax() , team_run_more_than_200.max())


# 17. Which team has conceded 200+ scores the most?
team_run_more_than_200.idxmax()

# 18. What was the highest run scored by a team in a single match?

totals.max()

# 19. Which is the biggest win in terms of run margin?
# Find the row with maximum win margin
biggest_win = matches_df.loc[matches_df['result_margin'].idxmax()]

print(biggest_win['winner'], biggest_win['result_margin'])


# 20. Which batsmen have played the most number of balls?

most_ball_played = ball_df.groupby('batsman')['ball'].idxmax().sort_values(ascending=False)
print(most_ball_played.idxmax())

# 21. Who are the leading run-scorers of all time?

leading_run_score = ball_df.groupby('batsman')['batsman_runs'].value_counts().sort_values(ascending=False)
print(leading_run_score.idxmax(),leading_run_score.max())

# 22. Who has hit the most number of 4's?

fours = ball_df[ball_df['batsman_runs']==4]
fours_max = fours['batsman'].value_counts()
print(fours_max.idxmax(),fours_max.max())

# 23. Who has hit the most number of 6's?

six = ball_df[ball_df['batsman_runs']==6]
most_six = six['batsman'].value_counts()
print(most_six.idxmax(), most_six.max())

# 24. Who has the highest strike rate?

# Exclude wides because they don’t count as a legal ball faced
valid_balls = ball_df[ball_df['extra_runs']==0]

# Step 1: Runs scored per batsman
runs = valid_balls.groupby('batsman')['total_runs'].sum()

# Step 2: Balls faced per batsman
balls = valid_balls.groupby('batsman').size()

# Step 3: Strike rate calculation
strike_rate = (runs / balls * 100).reset_index(name='strike_rate')

highest_sr = strike_rate.sort_values(by='strike_rate', ascending=False).head(1)
highest_sr

# 25. Who is the leading wicket-taker?
wicket = ball_df[ball_df['is_wicket']==1]
leading_wicket_taker = wicket['bowler'].value_counts()


print(leading_wicket_taker.idxmax(), leading_wicket_taker.max())

# both work same but second one give without run outs values

wicket = ball_df[ball_df['is_wicket']==1]
wicket = wicket[~wicket['dismissal_kind'].isin(['run out','retired hurt','obstructing the field'])]

leading_wicket_taker = wicket['bowler'].value_counts()

print(leading_wicket_taker.idxmax(), leading_wicket_taker.max())


# 26. Which stadium has hosted the most number of matches?

most_number_of_matches = matches_df['venue'].value_counts()
print(most_number_of_matches.idxmax() , most_number_of_matches.max())


# 27. Who has won the most MOM awards?

most_mom = matches_df['player_of_match'].value_counts()
print(most_mom.idxmax(), most_mom.max())

# 28. What is the count of fours hit in each season?

four = matches_df.merge(ball_df[['id','total_runs','batsman_runs']])
per_season  = four[four['batsman_runs']==4]
four_per_season = per_season.groupby('season')['batsman_runs'].value_counts()
four_per_season

# 29. What is the count of sixes hit in each season?
six = four[four['batsman_runs']==6]
six_per_season = six.groupby('season')['batsman_runs'].value_counts()
six_per_season

# 30. What is the count of runs scored from boundaries in each season?
run_scored_each_season = per_season.groupby('season')['batsman_runs'].sum()
run_scored_each_season

# 31. What is the run contribution from boundaries in each season?

run_contribution_from_boundries = run_scored_each_season.copy()
run_contribution_from_boundries

# 32. Which team has scored the most runs in the first 6 overs?
bat=ball_df[ball_df['over']<=6]
most_run_6over = bat.groupby('batting_team')['total_runs'].value_counts()
print(most_run_6over.idxmax(),most_run_6over.max())

# 33. Which team has scored the most runs in the last 4 overs?

most_four =  ball_df[ball_df['over']>=16]
most_run_4_four = most_four.groupby('batting_team')['total_runs'].value_counts()
print(most_run_4_four.idxmax(), most_run_4_four.max())

# 34. Which team has the best scoring run-rate in the first 6 overs?

first_6 = ball_df[ball_df['over']<=6]
best_run_rate_first_6over = first_6.grouaby('batting_team')['total_runs'].value_counts()
print(best_run_rate_first_6over.idxmax() , best_run_rate_first_6over.max())

# 35. Which team has the best scoring run-rate in the last 4 overs?
last_4 = ball_df[ball_df['over']>=16]
best_run_rate_last_4over = last_4.groupby('batting_team')['total_runs'].value_counts()
print(best_run_rate_last_4over.idxmax() , best_run_rate_last_4over.max())



