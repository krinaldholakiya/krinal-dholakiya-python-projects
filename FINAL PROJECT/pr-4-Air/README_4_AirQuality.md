<div align="center">

# -- ! Air Quality Index (AQI) — Data Analysis ! --
### *Exploratory Data Analysis on Global Air Pollution & Weather Data using Python*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)

<br/>

> *"Clean air starts with clean data — every reading tells us how the world is breathing."*

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

The **Air Quality Index (AQI) — Data Analysis** project is a Python-based EDA notebook that studies pollution levels (`PM2.5`, `PM10`, `NO2`, `SO2`, `CO`, `O3`) alongside weather conditions (`Temperature`, `Humidity`, `Wind Speed`, `Pressure`) across countries and cities.

This project is designed to:
- Strengthen understanding of `pandas`-based data cleaning and inspection
- Practice missing-value handling using mean imputation across 11 numeric columns
- Apply `groupby()` aggregation for country- and city-level pollution comparison
- Produce visually clear bar, pie, and histogram plots using `matplotlib`

---

## 🎯 Problem Statement

> **Objective:** Load, clean, and analyze the Air Quality dataset to uncover pollution trends by city and country.

You are given a raw CSV file (`dataset.csv`) containing pollutant and weather readings for multiple cities. The program must inspect the data, handle missing values, remove duplicates, and generate meaningful visual summaries that reveal which cities/countries face the worst air quality.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Inspection | Analysis | Shape, `info()`, head/tail preview |
| Missing Value Handling | Cleaning | Fills nulls in 11 numeric columns using mean |
| Duplicate Removal | Cleaning | Drops duplicate rows entirely |
| City/Country Comparison | Aggregation | Groups PM2.5 by Country, AQI by City |

The goal is to demonstrate **fundamental data analysis and visualization skills** through a clean, structured EDA notebook.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **Automated Data Loading** | Reads `dataset.csv` directly into a Pandas DataFrame |
| 👀 **Head/Tail Preview** | Displays first and last rows for a quick glance |
| 📐 **Structure Inspection** | Shape and `info()` summary of the dataset |
| 🔍 **Missing Value Detection** | Counts missing values per column |
| 🧹 **Mean Imputation** | Fills 11 numeric columns with their respective column mean |
| 🗑️ **Duplicate Removal** | Cleans repeated records using `drop_duplicates()` |
| 🧮 **NumPy Statistics** | Total, Average, Maximum, and Minimum AQI computed |
| 📶 **Bar Chart** | Average AQI grouped by City |
| 🥧 **Pie Chart** | AQI Category distribution |
| 📉 **Histogram** | PM2.5 frequency distribution |

---

## 🏗️ Project Structure

```
📦 air-quality-analysis/
│
├── 📄 4.ipynb               ← Main Jupyter notebook (entry point)
├── 📄 dataset.csv           ← Air Quality dataset
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
│ Clean: Fill Nulls w/ Mean    │
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
│ Group by Country / City      │
└────────────┬────────────────┘
             │
     ┌───────┴────────┬───────────────┐
     ▼                ▼               ▼
┌───────────┐   ┌─────────────┐  ┌───────────┐
│ Bar Chart │   │ Pie Chart   │  │ Histogram │
│ (City AQI)│   │ (Category)  │  │ (PM2.5)   │
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

print("Dataset Information")
df.info()
```

---

### 🔍 2. Detecting Missing Values

> Before cleaning, the notebook checks for null values across all pollutant and weather columns.

**Logic:**
```python
print("Missing Values")
print(df.isnull().sum())
```

---

### 🧹 3. Mean Imputation for Numeric Columns

> All 11 pollutant and weather columns are cleaned using **mean imputation**.

**Logic:**
```python
df["PM2.5"] = df["PM2.5"].fillna(df["PM2.5"].mean())
df["PM10"] = df["PM10"].fillna(df["PM10"].mean())
df["NO2"] = df["NO2"].fillna(df["NO2"].mean())
df["SO2"] = df["SO2"].fillna(df["SO2"].mean())
df["CO"] = df["CO"].fillna(df["CO"].mean())
df["O3"] = df["O3"].fillna(df["O3"].mean())
df["AQI"] = df["AQI"].fillna(df["AQI"].mean())
df["Temperature_C"] = df["Temperature_C"].fillna(df["Temperature_C"].mean())
df["Humidity_pct"] = df["Humidity_pct"].fillna(df["Humidity_pct"].mean())
df["WindSpeed_ms"] = df["WindSpeed_ms"].fillna(df["WindSpeed_ms"].mean())
df["Pressure_hPa"] = df["Pressure_hPa"].fillna(df["Pressure_hPa"].mean())
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🧮 `fillna(mean())` | Replaces nulls with the column's average value |
| 🗑️ `drop_duplicates()` | Removes fully duplicated rows |
| 📊 NumPy `sum/mean/max/min` | Quick statistical summary of the AQI column |

---

## 📊 Part B — Analysis & Visualization

### 🗑️ 4. Duplicate Removal & Statistical Summary

**Logic:**
```python
df.drop_duplicates(inplace=True)
print("Duplicate Records Removed")
print(df.shape)

df.describe()

aqi = np.array(df["AQI"])
print("Total AQI =", np.sum(aqi))
print("Average AQI =", np.mean(aqi))
print("Maximum AQI =", np.max(aqi))
print("Minimum AQI =", np.min(aqi))
```

---

### 🌍 5. Grouping by Country & City

**Logic:**
```python
country_pm = df.groupby("Country")["PM2.5"].mean()
print(country_pm)

city_aqi = df.groupby("City")["AQI"].mean()
print(city_aqi)
```

---

### 📶 6. Bar Chart — Average AQI by City

**Logic:**
```python
city_aqi.plot(kind="bar", color="skyblue", figsize=(8,5))
plt.title("Average AQI by City")
plt.xlabel("City")
plt.ylabel("Average AQI")
plt.xticks(rotation=45)
plt.show()
```

---

### 🥧 7. Pie Chart — AQI Category Distribution

**Logic:**
```python
df["AQI_Category"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(6,6)
)
plt.title("AQI Category Distribution")
plt.show()
```

---

### 📉 8. Histogram — PM2.5 Distribution

**Logic:**
```python
plt.figure(figsize=(8,5))
plt.hist(df["PM2.5"], bins=20, color="green")
plt.title("PM2.5 Distribution")
plt.xlabel("PM2.5")
plt.ylabel("Frequency")
plt.show()
```

**Sample Output:**
```
Total AQI = 48213.0
Average AQI = 96.4
Maximum AQI = 310.0
Minimum AQI = 12.0
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

- ✅ **Fully Cleaned Dataset** — All 11 numeric columns free of missing values, duplicates removed
- 🏙️ **City Comparison** — Average AQI clearly compared across cities
- 🥧 **Category Insight** — Proportional breakdown of AQI categories (Good, Moderate, Poor, etc.)
- 📉 **Distribution Insight** — Frequency spread of PM2.5 levels visualized
- 🧮 **Quick Stats** — Total, Average, Max, and Min AQI computed instantly with NumPy

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Core EDA concepts: cleaning, grouping, and plotting in one notebook |
| 🔄 **Reusability** | Cleaning logic can be reused for any similar environmental dataset |
| 📚 **Educational** | Demonstrates real-world missing value & duplicate handling |
| 🖥️ **Minimal Dependencies** | Runs with standard Python data-science libraries only |
| ⚡ **Lightweight** | Single-notebook workflow, runs top-to-bottom in seconds |
| 🧪 **Extensible** | Easy to add AQI prediction models or time-series trend analysis |
| 📖 **Readable Code** | Clear, sequential cells make the logic easy to follow |
| 🌍 **Actionable Insight** | Quickly identifies most/least polluted cities |

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

> *"The air we breathe is measured in numbers — and numbers tell us how to act."*

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
- 🌫️ [World Air Quality Index Project](https://waqi.info/) — Dataset inspiration

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 19 July, 2026*

</div>
