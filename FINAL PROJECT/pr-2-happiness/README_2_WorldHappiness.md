<div align="center">

# -- ! World Happiness Report — EDA & Visualization ! --
### *Exploratory Data Analysis on Global Happiness Factors using Python*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge)](https://seaborn.pydata.org/)

<br/>

> *"Happiness isn't just a feeling — it's data waiting to be understood."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 Part A — Data Loading & Cleaning](#-part-a--data-loading--cleaning)
- [📊 Part B — Visualization & Insights](#-part-b--visualization--insights)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **World Happiness Report — EDA & Visualization** project is a Python-based data analysis notebook that studies global happiness scores and their driving factors such as **GDP per Capita**, **Social Support**, **Healthy Life Expectancy**, **Freedom**, **Generosity**, and **Perceptions of Corruption**.

This project is designed to:
- Strengthen understanding of `pandas`-based data cleaning and inspection
- Practice missing-value handling using mean imputation
- Apply `groupby()` aggregation for regional and yearly comparisons
- Produce visually clear bar, line, and pie charts using `matplotlib`

---

## 🎯 Problem Statement

> **Objective:** Load, clean, and analyze the World Happiness dataset to uncover regional and yearly happiness trends.

You are given a raw CSV file (`dataset.csv`) containing happiness metrics for multiple countries across several years. The program must inspect the data, handle missing values, and generate meaningful visual summaries that reveal how economic, social, and freedom-related factors correlate with happiness.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Inspection | Analysis | Shape, columns, datatypes, and summary statistics |
| Missing Value Handling | Cleaning | Fills nulls in 9 numeric columns using mean |
| Regional Comparison | Aggregation | Groups Happiness Rank by Region |
| Yearly Trend | Aggregation | Groups GDP per Capita and Population by Year |

The goal is to demonstrate **fundamental data analysis and visualization skills** through a clean, structured EDA notebook.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **Automated Data Loading** | Reads `dataset.csv` directly into a Pandas DataFrame |
| 👀 **Head/Tail Preview** | Displays first and last 10 rows for a quick glance |
| 📐 **Structure Inspection** | Shape, column names, `info()`, `describe()`, and dtypes |
| 🔍 **Duplicate & Null Detection** | Counts duplicate rows and missing values per column |
| 🧹 **Mean Imputation** | Fills 9 numeric columns with their respective column mean |
| 🌍 **Unique Country Listing** | Displays all distinct countries in the dataset |
| 📶 **Bar Chart** | Happiness Rank grouped by Region |
| 📈 **Line Chart** | GDP per Capita trend across Years |
| 🥧 **Pie Chart** | Population share distribution by Year |
| 💾 **Optional Chart Export** | Saves any chart as a 300 DPI `.png` on user request |

---

## 🏗️ Project Structure

```
📦 world-happiness-analysis/
│
├── 📄 2.ipynb               ← Main Jupyter notebook (entry point)
├── 📄 dataset.csv           ← World Happiness dataset
├── 🖼️ barchart.png          ← Saved bar chart (optional output)
├── 🖼️ Linegraph.png         ← Saved line chart (optional output)
├── 🖼️ Piechart.png          ← Saved pie chart (optional output)
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
│   Import Libraries          │  ← NumPy, Pandas, Seaborn, Matplotlib
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Load dataset.csv          │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Inspect: shape, columns,    │
│ info, describe, dtypes      │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Detect Duplicates & Nulls   │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Clean: Fill Nulls w/ Mean   │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Explore Unique Countries    │
└────────────┬────────────────┘
             │
     ┌───────┴────────┬───────────────┐
     ▼                ▼               ▼
┌───────────┐   ┌─────────────┐  ┌───────────┐
│ Bar Chart │   │ Line Chart  │  │ Pie Chart │
│ (Region)  │   │ (GDP/Year)  │  │ (Pop/Yr)  │
└─────┬─────┘   └──────┬──────┘  └─────┬─────┘
      │                │               │
      ▼                ▼               ▼
┌─────────────────────────────────────────────┐
│   Prompt to Save Each Chart as PNG (opt.)    │
└───────────────────────────────────────────────┘
```

---

## 🧹 Part A — Data Loading & Cleaning

### 📝 1. Loading & Inspecting the Dataset

The dataset is read using `pandas.read_csv()` and immediately inspected using standard EDA calls.

**Logic:**
```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")
print("dataset loaded successfull!")

print("shape of dataset:", df.shape)
print("column of dataset:", df.columns)
print(df.info())
print(df.describe())
print(df.dtypes)
```

---

### 🔍 2. Detecting Duplicates & Missing Values

> Before cleaning, the notebook checks for duplicate rows and null values in every column.

**Logic:**
```python
print(df.duplicated().sum())
print(df.isnull().sum())
```

---

### 🧹 3. Mean Imputation for Numeric Columns

> All 9 key numeric columns are cleaned using **mean imputation** so no analysis step later fails due to missing data.

**Logic:**
```python
df["Happiness_Rank"] = df["Happiness_Rank"].fillna(df["Happiness_Rank"].mean())
df["Happiness_Score"] = df["Happiness_Score"].fillna(df["Happiness_Score"].mean())
df["GDP_per_Capita"] = df["GDP_per_Capita"].fillna(df["GDP_per_Capita"].mean())
df["Social_Support"] = df["Social_Support"].fillna(df["Social_Support"].mean())
df["Healthy_Life_Expectancy"] = df["Healthy_Life_Expectancy"].fillna(df["Healthy_Life_Expectancy"].mean())
df["Freedom_to_Make_Life_Choices"] = df["Freedom_to_Make_Life_Choices"].fillna(df["Freedom_to_Make_Life_Choices"].mean())
df["Generosity"] = df["Generosity"].fillna(df["Generosity"].mean())
df["Perceptions_of_Corruption"] = df["Perceptions_of_Corruption"].fillna(df["Perceptions_of_Corruption"].mean())
df["Population_Millions"] = df["Population_Millions"].fillna(df["Population_Millions"].mean())
df["Unemployment_Rate"] = df["Unemployment_Rate"].fillna(df["Unemployment_Rate"].mean())
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🧮 `fillna(mean())` | Replaces nulls with the column's average value |
| 🔁 Column-wise Cleaning | Applied individually to all 9 numeric fields |
| 🌍 `unique()` | Lists distinct country names present in the dataset |

---

## 📊 Part B — Visualization & Insights

### 📶 4. Bar Chart — Happiness Rank by Region

**Logic:**
```python
Region = df.groupby("Region")["Happiness_Rank"].sum()
plt.figure(figsize=(10,5))
plt.bar(Region.index, Region.values, color="skyblue")
plt.xticks(rotation=45)
plt.title("Happiness_Rank By Region")
plt.xlabel("Region")
plt.ylabel("Happiness_Rank")
plt.show()
```

---

### 📈 5. Line Chart — GDP per Capita by Year

**Logic:**
```python
Year = df.groupby("Year")["GDP_per_Capita"].sum()
plt.figure(figsize=(10,5))
plt.plot(Year.index, Year.values, marker="o", color="red")
plt.title("GDP_per_Capita by Year")
plt.xlabel("Year")
plt.ylabel("GDP_per_Capita")
plt.grid(True)
plt.show()
```

---

### 🥧 6. Pie Chart — Population Share by Year

**Logic:**
```python
Year = df.groupby("Year")["Population_Millions"].sum()
plt.figure(figsize=(8,8))
plt.pie(Year.values, labels=Year.index, autopct="%1.1f%%", startangle=90)
plt.title("Population by Year")
plt.show()
```

**Sample Output (console prompt shown for every chart):**
```
Do you want to save graph (yes/no): yes
Graph Saved Successfully!
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🐼 **Pandas** | Latest | Data loading, cleaning & aggregation |
| 🔢 **NumPy** | Latest | Numerical operations |
| 📊 **Matplotlib** | Latest | Bar, line & pie chart visualization |
| 🎨 **Seaborn** | Latest | Statistical styling support |
| 📓 **Jupyter Notebook** | Latest | Interactive development environment |

---

## 📈 Results & Insights

After running the notebook, the following outputs are produced:

- ✅ **Fully Cleaned Dataset** — All 9 numeric columns free of missing values
- 🌍 **Regional Insight** — Happiness Rank clearly compared across all Regions
- 📈 **Economic Trend** — GDP per Capita trend visualized year-over-year
- 🥧 **Population Insight** — Year-wise population share visualized proportionally
- 💾 **Optional Export** — Each chart can be saved as a high-resolution PNG

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Core EDA concepts: cleaning, grouping, and plotting in one notebook |
| 🔄 **Reusability** | Cleaning logic can be reused for any similar tabular dataset |
| 📚 **Educational** | Demonstrates real-world missing value handling with mean imputation |
| 🖥️ **Minimal Dependencies** | Runs with standard Python data-science libraries only |
| ⚡ **Lightweight** | Single-notebook workflow, runs top-to-bottom in seconds |
| 🧪 **Extensible** | Easy to add correlation heatmaps or predictive models |
| 📖 **Readable Code** | Clear, sequential cells make the logic easy to follow |
| 🛡️ **Safe Charting** | Save-prompt avoids unwanted file clutter on every run |

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

> *"Every dataset tells a story — happiness data tells the story of the world."*

**🎓 Role:** Data Analyst | Python Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · Pandas · NumPy · Data Visualization · EDA

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Pandas Official Docs](https://pandas.pydata.org/docs/) — Official Pandas reference
- 📊 [Matplotlib Documentation](https://matplotlib.org/stable/contents.html) — Visualization guide
- 🎨 [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical plotting reference
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Data analysis courses
- 🌍 [World Happiness Report](https://worldhappiness.report/) — Dataset inspiration

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 19 July, 2026*

</div>
