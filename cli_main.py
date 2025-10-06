import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore,Style,init
from tabulate import tabulate

print("T20 WORLD CUP ANALYZER")
def load_file():
    filename = input("Enter ur csv file: ")
    if not filename.endswith(".csv"):
        print("❌ Error! PLease enter a csv file:")
        return None
    
    try:
        df = pd.read_csv(filename)
        print("✅ File loaded successfully")
        return df
    except FileNotFoundError:
        print("❌ Invalid File. Please check if the file is valid")
        return None
    

def get_total_runs(df):
    team1 = df[["Team1", "Runs_Team1"]].rename(columns={"Team1": "Team", "Runs_Team1": "Runs"})
    team2 = df[["Team2", "Runs_Team2"]].rename(columns={"Team2": "Team", "Runs_Team2": "Runs"})
    all_runs = pd.concat([team1, team2])
    total_runs = all_runs.groupby("Team")["Runs"].sum().reset_index()
    print("Total Runs by Teams:")
    print(tabulate(total_runs, headers="keys", tablefmt="pretty"))
    return total_runs

def get_top_batsman(df):
    Top = df["Runs_Scorer"].idxmax()
    top_batsmen = df.loc[Top, "Top_Scorer"]
    most_runs = df.loc[Top, "Runs_Scorer"]
    print(f"The top batsmen is {top_batsmen} with {most_runs} runs")
    return f"The top batsman is {top_batsmen} with {most_runs} runs"

def get_top_bowler(df):
    top_bowler = df["Wickets_Bowler"].idxmax()
    top_bowlers = df.loc[top_bowler, "Top_Bowler"]
    most_wckts = df.loc[top_bowler, "Wickets_Bowler"]
    print(f"The top wicket taker is {top_bowlers} with {most_wckts} wickets")
    return f"The top wicket taker is {top_bowlers} with {most_wckts} wickets"

def get_top_5_batsmen(df, n=5, return_df=False):
    top5 = df.sort_values(by="Runs_Scorer", ascending=False).head(n)
    if return_df:
        return top5
    table = top5[["Top_Scorer", "Runs_Scorer"]]
    print("The Top 5 Batsmen are:")
    print(tabulate(table.values, headers=table.columns, tablefmt="pretty"))
    results = [f"{row['Top_Scorer']} - {row['Runs_Scorer']} runs" for _, row in top5.iterrows()]
    return results
    
def get_top_5_bowlers(df, n=5, return_df=False):
    top_wickets = df.sort_values(by="Wickets_Bowler", ascending=False).head(n)
    if return_df:
        return top_wickets
    table = top_wickets[["Top_Bowler", "Wickets_Bowler"]]
    print("The Top 5 Bowlers with the most wicket are:")
    print(tabulate(table.values, headers=table.columns, tablefmt="pretty"))
    results1 = [f"{row['Top_Bowler']} - {row['Wickets_Bowler']} wickets" for _, row in top_wickets.iterrows()]
    return results1


def most_wins(df):
    winner = df["Winner"].value_counts().idxmax() #counting how many times each team appears as winners
    print(f"The team with the most wins is {winner} ")
    return f"Team with most wins is {winner}"


def win_percent(df, return_df=False):
    played = pd.concat([df["Team1"], df["Team2"]]).value_counts()
    wins = df["Winner"].value_counts()
    percentage = (wins / played * 100).round(2).fillna(0).sort_values(ascending=False) #Cal %, fills nan as 0 nd gives descending ie highest value first
    
    p_df = percentage.reset_index()
    p_df.columns = ["Team", "Win %"]
    if return_df:
        return p_df
    print("Win Percentage:")
    print(tabulate(p_df, headers=p_df.columns, tablefmt="pretty"))
    return p_df


def save_analysis(df):
     # Compute everything
    total_runs = get_total_runs(df)
    top5 = get_top_5_batsmen(df, return_df=True)
    top_wickets = get_top_5_bowlers(df, return_df=True)
    win_perc = win_percent(df, return_df=True)
    
    # Top batsman & bowler (single row DataFrame for Excel)
    top_batsman = pd.DataFrame([{"Top Batsman": get_top_batsman(df).split(" with ")[0]}])
    top_bowler = pd.DataFrame([{"Top Bowler": get_top_bowler(df).split(" with ")[0]}])
    
    # Save to Excel with multiple sheets
    with pd.ExcelWriter("analyzed_t20.xlsx") as writer:
        total_runs.to_excel(writer, sheet_name="Total Runs", index=False)
        top5.to_excel(writer, sheet_name="Top 5 Batsmen", index=False)
        top_wickets.to_excel(writer, sheet_name="Top 5 Bowlers", index=False)
        win_perc.to_excel(writer, sheet_name="Win Percentages", index=False)
        top_batsman.to_excel(writer, sheet_name="Top Batsman", index=False)
        top_bowler.to_excel(writer, sheet_name="Top Bowler", index=False)

    print("✅ Saved analysis as analyzed_t20.xlsx")

    

def visualize(df, total_runs, top5, top_wickets):
    plt.figure(figsize=(8,5))
    plt.bar(total_runs["Team"], total_runs["Runs"], color="green")
    plt.title("Team runs comparison chart") 
    plt.xlabel("Teams")
    plt.ylabel("Runs")
    plt.savefig("Team_runs_comparison.png")
    plt.close()

#Top 5 run scorers Bar chart
    plt.figure(figsize=(9,5))
    plt.bar(top5["Top_Scorer"], top5["Runs_Scorer"], color="red")
    plt.title("Top 5 Batsmen")
    plt.xlabel("Players")
    plt.ylabel("Runs")
    plt.savefig("Top5_batsmen.png")
    plt.close()

#Top 5 wicket takers bar
    plt.figure(figsize=(9,5))
    plt.bar(top_wickets["Top_Bowler"], top_wickets["Wickets_Bowler"], color="purple")
    plt.title("Top 5 Wicket takers")
    plt.xlabel("Players")
    plt.ylabel("Wickets")
    plt.savefig("Top5_wickets.png")
    plt.close()


#win % pie chart
    plt.figure()
    why = df["Winner"].value_counts()
    plt.pie(why.values, labels=why.index, autopct="%1.1f%%", startangle=90)
    plt.title("Winning Percentage of Teams")
    plt.savefig("Winning_percntage.png")
    plt.close()



def main():
    df = load_file()
    if df is None:
        return
    while True:
        print("1. Total Runs")
        print("2. Top Batsman")
        print("3. Top Bowler")
        print("4. Top 5 Batsmen")
        print("5. Top 5 Bowlers")
        print("6. Win Percentage")
        print("7. Most wins by a team")
        print("8. Visulaize")
        print("9. Exit")
        choice = input("Select any option:")

        if choice == "1":
            total_runs = get_total_runs(df)
        elif choice == "2":
            get_top_batsman(df)
        elif choice == "3":
            get_top_bowler(df)
        elif choice == "4":
            top5 =  get_top_5_batsmen(df)
        elif choice == "5":
            top_wickets = get_top_5_bowlers(df)
        elif choice == "6":
            win_percent(df)
        elif choice == "7":
            most_wins(df)
        elif choice == "8":
            total_runs = get_total_runs(df)
            top5 = get_top_5_batsmen(df, return_df=True)
            top_wickets = get_top_5_bowlers(df, return_df=True)
            visualize(df, total_runs, top5, top_wickets)
            print("✅ Charts saved successfully")
        elif choice == "9":
            print(" Exiting...")
            save_analysis(df)
            break

        else:
            print("❌ Invalid choice! Please try again")

 
if __name__ == "__main__":
    main()
            



