# 🏆 T20 World Cup Analyzer

A Python-based cricket analytics project that provides match insights, player rankings, and visualizations using both **CLI** and **Streamlit** interfaces.

---

## 📋 **Project Overview**
The **T20 World Cup Analyzer** helps users upload match data and explore in-depth statistics such as:
- Total runs scored by each team  
- Top batsmen and bowlers  
- Win percentages  
- Most successful team  
- Top 5 batsmen and bowlers  
- Visualizations for team and player performances  

It includes:
- A **CLI version** for command-line analysis  
- A **Streamlit web app** for interactive exploration and downloads  

---

## ⚙️ **Tech Stack**
- **Python 3.10+**
- **Pandas** — data manipulation  
- **Matplotlib & Seaborn** — data visualization  
- **Tabulate** — pretty CLI tables  
- **Streamlit** — web dashboard  
- **Colorama** — colored CLI text  
- **XlsxWriter** — export reports to Excel  

---

## 🚀 **Features**
- Analyze team and player performance in T20 World Cups  
- View top-performing batsmen and bowlers  
- Get team-wise win percentages  
- Save analysis results as an Excel report  
- Generate visual insights (bar and pie charts)  

---

## 🧮 **Visualizations**
- Team Runs Comparison Chart  
- Top 5 Batsmen Bar Chart  
- Top 5 Wicket Takers Chart  
- Win Percentage Pie Chart  

All charts are saved as `.png` images automatically.

---

## 💻 **How to Run (CLI Version)**
1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/T20-WorldCup-Analyzer.git
   cd T20-WorldCup-Analyzer
   ```

---

Install dependencies:
pip install -r requirements.txt

---

Run the CLI version:
```bash
python cli_main.py
```

Upload your CSV file when prompted.

---

## 🚀 Live App
👉 [View the app here](https://cricket-analysis-00.streamlit.app/)

---

🌐 How to Run (Streamlit App)

1. Install dependencies (if not done already):
   pip install -r requirements.txt

2. Run the Streamlit app:
   streamlit run main_app.py

3. Upload your dataset and explore:

- View stats

- Download analyzed Excel report

- Visualize key insights

---

📁 Output Files

After analysis, the following files will be generated:

analyzed_t20.xlsx — complete insights in Excel

Top5_batsmen.png, Top5_wickets.png, Winning_percentage.png, etc

---

📸 Preview:

UI
<img width="1920" height="1034" alt="UI" src="https://github.com/user-attachments/assets/8bd7273b-7767-4d2a-955e-7aa3ea9f2d3c" />

----------------------------------------------------------------------------------------------------------------------------------


Sample CSV:
<img width="1920" height="1034" alt="demo" src="https://github.com/user-attachments/assets/873a4f82-765b-47a8-bda1-abc9743eb1b8" />



