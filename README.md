 # 🏏 IPL Data Analysis (2008–2020)

This project explores **IPL Ball-by-Ball (2008–2020)** and **Match datasets** to uncover insights about team performances, players, venues, and toss decisions. Using **Python, Pandas, Matplotlib, and Seaborn**, we answer 35+ cricket analytics questions with visualizations.  

---

## 📊 Dataset Overview
- **Ball-by-Ball dataset** (`IPL Ball-by-Ball 2008-2020.csv`)  
  Contains every delivery bowled in IPL matches (2008–2020).  

- **Match dataset** (`IPL Matches 2008-2020.csv`)  
  Contains high-level match details like teams, toss, umpires, results, and venues.  

---

## 🔧 Tools & Libraries
- **Python 3**  
- **Pandas** → Data manipulation  
- **Matplotlib** & **Seaborn** → Data visualization  

---

## 📌 Key Insights & Visualizations

### 1. Matches Played Per Season
📈 The number of matches varied across seasons, peaking in **2013** with 76 matches.  

![Question 7](images/Question7.png)




---

### 2. Toss Decisions Across Seasons
🟢 Teams initially preferred to **bat** after winning the toss, but after 2014 the preference shifted strongly towards **fielding**.  

![Toss Decision by Season](images/Question7.png)

---

### 3. Runs Scored Each Season
- Highest runs scored in a season: **2013**  
- Consistent scoring trends after 2014 as match count stabilized.  

---

### 4. Does Winning Toss Help Win the Match?
- Winning toss does **not guarantee victory**.  
- Only **~51%** of toss winners went on to win the match.  

---

### 5. Chasing vs. Defending Wins
- Chasing teams have a **higher success rate** in IPL history.  

---

### 6. Most Successful Teams
- **Most Matches Won:** *[Team Name]*  
- **Highest Win %:** *[Team Name]*  

---

### 7. Player & Team Achievements
- **Most 200+ Scores by a Team:** *[Team Name]*  
- **Highest Individual Team Score:** *[Runs]*  
- **Leading Run-Scorer:** *[Player Name]*  
- **Most Sixes:** *[Player Name]*  
- **Most Fours:** *[Player Name]*  
- **Highest Strike Rate (min balls faced):** *[Player Name]*  
- **Leading Wicket-Taker:** *[Bowler Name]*  
- **Most MOM Awards:** *[Player Name]*  

---

### 8. Venue Insights
- **Most Matches Hosted:** *[Stadium Name]*  
- Certain teams have “lucky” venues where they dominate consistently.  

---

### 9. Innings-Wise Performance
- Some teams perform better while chasing, while others dominate when batting first.  

---

### 10. Powerplay & Death Overs
- **Best Powerplay (0–6 overs) team:** *[Team Name]*  
- **Best Death Overs (16–20 overs) team:** *[Team Name]*  

---

## 📂 Project Structure
├── IPL Ball-by-Ball 2008-2020.csv
├── IPL Matches 2008-2020.csv
├── analysis.ipynb # Jupyter notebook with all 35 Q&A analysis
├── README.md # Project documentation
├── images/ # Visualizations and plots


---

## 🚀 Future Work
- Predict match outcomes using ML models.  
- Player performance forecasting.  
- Venue-specific batting/bowling advantage analysis.  

---

## ✨ Conclusion
This analysis shows that:
1. Toss does not heavily influence match outcomes.  
2. Chasing has been more successful in IPL history.  
3. Few players and teams consistently dominate across multiple seasons.  

---

## 🙌 Acknowledgments
- Dataset: [Kaggle IPL Dataset 2008–2020]  
- Tools: Python, Pandas, Matplotlib, Seaborn  
