<div align="center">

# -- ! Stock Market Dataset — Financial Analysis ! --
### *Exploratory Data Analysis on Stock Prices, Volume & Sector Trends using Python*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)

<br/>

> *"Every candle on a chart hides a story of numbers — data helps us read it clearly."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 Part A — Data Loading & Cleaning](#-part-a--data-loading--cleaning)
- [📊 Part B — Analysis & Visualization](#-part-b--analysis--visualization)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Stock Market Dataset — Financial Analysis** project is a Python-based EDA notebook that studies stock pricing (`Open`, `High`, `Low`, `Close`, `Adj_Close`), `Volume`, `Market Cap`, and `Daily Returns` across multiple tickers and sectors.

This project is designed to:
- Strengthen understanding of `pandas`-based data cleaning and inspection
- Practice missing-value handling using both **mean** and **median** imputation
- Apply `groupby()` aggregation for sector-wise financial comparison
- Produce visually clear bar, pie, and histogram plots using `matplotlib`

---

## 🎯 Problem Statement

> **Objective:** Load, clean, and analyze the Stock Market dataset to uncover sector-wise pricing and return trends.

You are given a raw CSV file (`dataset.csv`) containing daily stock records for multiple tickers. The program must inspect the data, handle missing values, remove duplicates, and generate meaningful visual summaries that reveal how different sectors perform.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Inspection | Analysis | Shape, `info()`, head/tail preview |
| Missing Value Handling | Cleaning | Fills nulls using mean (prices) & median (volume) |
| Duplicate Removal | Cleaning | Drops duplicate rows entirely |
| Sector Comparison | Aggregation | Groups Close price & Market Cap by Sector |

The goal is to demonstrate **fundamental data analysis and visualization skills** through a clean, structured EDA notebook.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **Automated Data Loading** | Reads `dataset.csv` directly into a Pandas DataFrame |
| 👀 **Head/Tail Preview** | Displays first and last rows for a quick glance |
| 📐 **Structure Inspection** | Shape and `info()` summary of the dataset |
| 🔍 **Missing Value Detection** | Counts missing values per column |
| 🧹 **Mean/Median Imputation** | Fills price columns with mean, `Volume` with median |
| 🗑️ **Duplicate Removal** | Cleans repeated records using `drop_duplicates()` |
| 🧮 **NumPy Statistics** | Total, Average, Maximum, and Minimum Close price computed |
| 📶 **Bar Chart** | Average Closing Price grouped by Sector |
| 🥧 **Pie Chart** | Sector-wise stock distribution |
| 📉 **Histogram** | Daily Return (%) frequency distribution |

---

## 🏗️ Project Structure

```
📦 stock-market-analysis/
│
├── 📄 5.ipynb               ← Main Jupyter notebook (entry point)
├── 📄 dataset.csv           ← Stock Market dataset
│
└── 📄 README.md             ← Project documentation
```

---

## 🔄 Project Workflow

```
Notebook Start
      │
      ▼
┌─────────────────────────────┐
│   Import Libraries          │  ← Pandas, NumPy, Matplotlib
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Load dataset.csv          │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Inspect: shape, info,       │
│ head/tail preview           │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Detect Missing Values        │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Clean: Mean (price) /        │
│ Median (Volume)              │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Remove Duplicate Records     │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ describe() + NumPy Stats     │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Group by Sector               │
└────────────┬────────────────┘
             │
     ┌───────┴────────┬───────────────┐
     ▼                ▼               ▼
┌───────────┐   ┌─────────────┐  ┌───────────┐
│ Bar Chart │   │ Pie Chart   │  │ Histogram │
│ (Sector)  │   │ (Sector)    │  │ (Return%) │
└───────────┘   └─────────────┘  └───────────┘
```

---

## 🧹 Part A — Data Loading & Cleaning

### 📝 1. Loading & Inspecting the Dataset

The dataset is read using `pandas.read_csv()` and immediately inspected using standard EDA calls.

**Logic:**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")
print("Dataset Loaded Successfully")
df.head()

print("Shape of Dataset")
print(df.shape)

df.info()
```

---

### 🔍 2. Detecting Missing Values

> Before cleaning, the notebook checks for null values across all pricing and volume columns.

**Logic:**
```python
print(df.isnull().sum())
```

---

### 🧹 3. Mean & Median Imputation

> Price-related columns are cleaned using **mean imputation**, while `Volume` uses **median imputation** since trading volume can be highly skewed.

**Logic:**
```python
df["Open"] = df["Open"].fillna(df["Open"].mean())
df["High"] = df["High"].fillna(df["High"].mean())
df["Low"] = df["Low"].fillna(df["Low"].mean())
df["Close"] = df["Close"].fillna(df["Close"].mean())
df["Adj_Close"] = df["Adj_Close"].fillna(df["Adj_Close"].mean())
df["Volume"] = df["Volume"].fillna(df["Volume"].median())
df["Market_Cap_B"] = df["Market_Cap_B"].fillna(df["Market_Cap_B"].mean())
df["Daily_Return_pct"] = df["Daily_Return_pct"].fillna(df["Daily_Return_pct"].mean())
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🧮 `fillna(mean())` | Used for price & return columns |
| 📊 `fillna(median())` | Used for `Volume` to reduce skew impact |
| 🗑️ `drop_duplicates()` | Removes fully duplicated rows |

---

## 📊 Part B — Analysis & Visualization

### 🗑️ 4. Duplicate Removal & Statistical Summary

**Logic:**
```python
df.drop_duplicates(inplace=True)
print("Duplicate Records Removed")
print(df.shape)

df.describe()

print(df["Ticker"].unique())
print(df["Sector"].unique())

price = np.array(df["Close"])
print("Total =", np.sum(price))
print("Average =", np.mean(price))
print("Maximum =", np.max(price))
print("Minimum =", np.min(price))
```

---

### 🏢 5. Grouping by Sector

**Logic:**
```python
sector_close = df.groupby("Sector")["Close"].mean()
print(sector_close)

sector_market = df.groupby("Sector")["Market_Cap_B"].mean()
print(sector_market)
```

---

### 📶 6. Bar Chart — Average Closing Price by Sector

**Logic:**
```python
sector_close.plot(kind="bar", color="skyblue", figsize=(8,5))
plt.title("Average Closing Price by Sector")
plt.xlabel("Sector")
plt.ylabel("Close Price")
plt.xticks(rotation=45)
plt.show()
```

---

### 🥧 7. Pie Chart — Sector Distribution

**Logic:**
```python
df["Sector"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(6,6)
)
plt.title("Sector Distribution")
plt.ylabel("")
plt.show()
```

---

### 📉 8. Histogram — Daily Return Distribution

**Logic:**
```python
plt.figure(figsize=(8,5))
plt.hist(df["Daily_Return_pct"], bins=20, color="green")
plt.title("Daily Return Distribution")
plt.xlabel("Daily Return (%)")
plt.ylabel("Frequency")
plt.show()
```

**Sample Output:**
```
Total = 184532.7
Average = 142.6
Maximum = 812.4
Minimum = 8.2
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🐼 **Pandas** | Latest | Data loading, cleaning & aggregation |
| 🔢 **NumPy** | Latest | Numerical statistics (sum, mean, max, min) |
| 📊 **Matplotlib** | Latest | Bar, pie & histogram visualization |
| 📓 **Jupyter Notebook** | Latest | Interactive development environment |

---

## 📈 Results & Insights

After running the notebook, the following outputs are produced:

- ✅ **Fully Cleaned Dataset** — All pricing/volume columns free of missing values, duplicates removed
- 🏢 **Sector Comparison** — Average Closing Price clearly compared across sectors
- 🥧 **Distribution Insight** — Proportional breakdown of stocks per sector
- 📉 **Volatility Insight** — Daily Return (%) frequency spread visualized
- 🧮 **Quick Stats** — Total, Average, Max, and Min Close price computed instantly with NumPy

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Core EDA concepts: cleaning, grouping, and plotting in one notebook |
| 🔄 **Reusability** | Cleaning logic can be reused for any similar financial dataset |
| 📚 **Educational** | Demonstrates real-world mean/median imputation strategy selection |
| 🖥️ **Minimal Dependencies** | Runs with standard Python data-science libraries only |
| ⚡ **Lightweight** | Single-notebook workflow, runs top-to-bottom in seconds |
| 🧪 **Extensible** | Easy to add moving averages, trend-lines, or price prediction models |
| 📖 **Readable Code** | Clear, sequential cells make the logic easy to follow |
| 💹 **Actionable Insight** | Quickly identifies best/worst performing sectors |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Your Name

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourhandle)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yourhandle/)

> *"Numbers move markets — but understanding them moves careers."*

**🎓 Role:** Data Analyst | Python Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · Pandas · NumPy · Data Visualization · EDA

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Pandas Official Docs](https://pandas.pydata.org/docs/) — Official Pandas reference
- 📊 [Matplotlib Documentation](https://matplotlib.org/stable/contents.html) — Visualization guide
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Data analysis courses
- 💹 [Yahoo Finance](https://finance.yahoo.com/) — Dataset inspiration

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 19 July, 2026*

</div>
