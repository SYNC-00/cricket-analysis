import streamlit as st
import pandas as pd
from cli_main import get_total_runs,get_top_batsman,get_top_bowler,get_top_5_batsmen,get_top_5_bowlers,win_percent,most_wins,visualize
from io import BytesIO
st.title("📊 T20 Cricket Analyzer")
upload = st.file_uploader("📂 Upload ur csv file", type=["csv"])

if upload:
    df = pd.read_csv(upload)

    if st.button("🏏 Show Total Runs"):
        total_runs = get_total_runs(df)
        st.success("✅ Done!")
        st.dataframe(total_runs)


    if st.button("🏏 Show Top Batsman"):
        result = get_top_batsman(df)
        st.success("✅ Done!")
        st.write("->",result)

    if st.button("🎯 Show Top Bowler"):
        result2 = get_top_bowler(df)
        st.success("✅ Done!")
        st.write("->",result2)

    if st.button("🏏 Top 5 Batsmen"):
        top5 =  get_top_5_batsmen(df)
        st.success("✅ Done!")
        for line in top5:
            st.write("->",line)

    if st.button("🎯 Top 5 Bowlers"):
        top_wickets = get_top_5_bowlers(df)
        st.success("✅ Done!")
        for line in top_wickets:
            st.write("->",line)
     
    if st.button("📊 Show win percentage"):
        Wins = win_percent(df, return_df=True)
        st.success("✅ Done!")
        st.dataframe(Wins)

    if st.button("🏆 Most Wins Team"):
        result = most_wins(df)
        st.success("✅ Done!")
        st.write("->",result) 

    if st.button("📊 Visualize"):
        total_runs = get_total_runs(df)
        top5 = get_top_5_batsmen(df, return_df=True)
        top5_list = get_top_5_batsmen(df)
        top_wickets = get_top_5_bowlers(df, return_df=True)
        top_wickets_list = get_top_5_bowlers(df)
        visualize(df, total_runs, top5, top_wickets)
        st.success("✅ Charts downloaded successfully")

        for line in top5_list:
            st.write(line)
        for line in top_wickets_list:
            st.write(line)

    if st.button("💾 Save Analyzed Report "):
        total_runs = get_total_runs(df)
        top5 = get_top_5_batsmen(df, return_df=True)
        top_wickets = get_top_5_bowlers(df, return_df=True)
        win_perc = win_percent(df, return_df=True)
    
        top_batsman = pd.DataFrame([{"Top Batsman": get_top_batsman(df).split(" with ")[0]}])
        top_bowler = pd.DataFrame([{"Top Bowler": get_top_bowler(df).split(" with ")[0]}])

    # Save to Excel in memory
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            total_runs.to_excel(writer, sheet_name="Total Runs", index=False)
            top5.to_excel(writer, sheet_name="Top 5 Batsmen", index=False)
            top_wickets.to_excel(writer, sheet_name="Top 5 Bowlers", index=False)
            win_perc.to_excel(writer, sheet_name="Win Percentages", index=False)
            top_batsman.to_excel(writer, sheet_name="Top Batsman", index=False)
            top_bowler.to_excel(writer, sheet_name="Top Bowler", index=False)
        output.seek(0)

        st.success("✅ Excel file ready for download")
        st.download_button(
            label="📥 Download Excel",
            data=output,
            file_name="analyzed_t20.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
