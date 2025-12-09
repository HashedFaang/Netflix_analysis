# 🎬 Netflix Data Analysis using Python & Pandas

## 📌 Project Overview  
This project analyzes Netflix-style viewing data to understand user behavior, genre preferences, engagement levels, and content performance.  
It uses **Python + Pandas** for data cleaning, transformation, and exploratory data analysis (EDA).  
The goal is to uncover patterns such as which genres users prefer, how much they watch, and which titles perform best.

---

## 🎯 Objectives  
- Clean and preprocess raw transaction-like viewing data  
- Identify viewing trends across genres and users  
- Compute an engagement metric (`watch_time / duration`)  
- Rank titles by average rating and engagement  
- Group similar movies using simple genre-based logic  

---

## 🛠️ Tech Stack  
- **Python**  
- **Pandas**  
- **NumPy**  
- **Matplotlib (optional)**  
- **VS Code / Jupyter Notebook**  

---

## 📂 Project Structure
## 📂 Project Structure
```
├── netflix_data.csv          # Sample dataset
├── netflix_analysis.py       # Python analysis script
└── README.md                 # Documentation
```

## 🔍 Key Analysis Performed  

### ✔ Data Cleaning  
- Removed missing & duplicate records  
- Ensured correct data formats  

### ✔ Exploratory Data Analysis (EDA)  
- Genre distribution  
- Top-rated movies  
- User viewing activity  
- Watch-duration patterns  

### ✔ Engagement Score  
A simple metric to measure how long users stayed interested:engagement = watch_time / duration
### ✔ Genre-Based Similar Titles  
Grouped movies based on genre using Pandas: Action → [Movie_5, Movie_11, Movie_20]
Comedy → [Movie_3, Movie_7, Movie_13
---

## 📊 Sample Insights  
- **Drama & Action** are the most-watched genres  
- Shorter-duration movies show **higher engagement**  
- Night-time viewing tends to have **lower completion rates**  
- Some titles consistently receive **higher average ratings**  

---

## 🚀 How to Run  
```bash
pip install pandas
python netflix_analysis.py
