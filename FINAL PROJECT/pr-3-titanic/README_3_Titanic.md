<div align="center">

# -- ! Titanic Dataset — Survival Analysis ! --
### *Exploratory Data Analysis on Passenger Demographics & Survival using Python*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge)](https://seaborn.pydata.org/)

<br/>

> *"Every passenger had a story — the data just helps us read between the lines."*

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

The **Titanic Dataset — Survival Analysis** project is a Python-based EDA notebook that explores passenger records from the Titanic disaster. It studies how **gender**, **passenger class**, and **ticket details** relate to **survival outcomes**.

This project is designed to:
- Strengthen understanding of `pandas`-based data cleaning and inspection
- Practice handling missing values across mixed data types (numeric & categorical)
- Apply `groupby()` aggregation to compare survival by gender and class
- Produce visually clear bar, line, and pie charts using `matplotlib`

---

## 🎯 Problem Statement

> **Objective:** Load, clean, and analyze the Titanic dataset to uncover survival patterns across gender and passenger class.

You are given a raw CSV file (`dataset.csv`) containing passenger-level Titanic records. The program must inspect the data, handle missing values in both numeric and categorical columns, and generate meaningful visual summaries of survival trends.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Inspection | Analysis | Shape, columns, datatypes, and summary statistics |
| Missing Value Handling | Cleaning | Fills nulls in Age, Fare, Cabin, and Embarked |
| Gender Comparison | Aggregation | Groups Survived count by Sex |
| Class Comparison | Aggregation | Groups Ticket count by Pclass |

The goal is to demonstrate **fundamental data analysis and visualization skills** through a clean, structured EDA notebook.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **Automated Data Loading** | Reads `dataset.csv` directly into a Pandas DataFrame |
| 👀 **Head/Tail Preview** | Displays first and last 10 rows for a quick glance |
| 📐 **Structure Inspection** | Shape, column names, `info()`, `describe()`, and dtypes |
| 🔍 **Duplicate & Null Detection** | Counts duplicate rows and missing values per column |
| 🧹 **Mixed-Type Cleaning** | Fills `Age`, `Fare`, `Cabin`, and `Embarked` appropriately |
| 📶 **Bar Chart** | Survived count grouped by Sex |
| 📈 **Line Chart** | Ticket count trend across Passenger Class |
| 🥧 **Pie Chart** | Ticket share distribution by Sex |
| 💾 **Optional Chart Export** | Saves any chart as a 300 DPI `.png` on user request |

---

## 🏗️ Project Structure

```
📦 titanic-survival-analysis/
│
├── 📄 3.ipynb               ← Main Jupyter notebook (entry point)
├── 📄 dataset.csv           ← Titanic dataset
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
│ Clean: Age/Fare/Cabin/Emb.  │
└────────────┬────────────────┘
             │
     ┌───────┴────────┬───────────────┐
     ▼                ▼               ▼
┌───────────┐   ┌─────────────┐  ┌───────────┐
│ Bar Chart │   │ Line Chart  │  │ Pie Chart │
│ (Sex)     │   │ (Pclass)    │  │ (Sex)     │
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

### 🧹 3. Cleaning Numeric & Categorical Columns

> Unlike purely numeric datasets, Titanic requires different fill strategies for different column types.

**Logic:**
```python
df["Age"] = df["Age"].fillna("")
df["Fare"] = df["Fare"].fillna(df["Fare"].mean())
df["Cabin"] = df["Cabin"].fillna("-")
df["Embarked"] = df["Embarked"].fillna("-")
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🧮 `fillna(mean())` | Used for the numeric `Fare` column |
| 🔤 `fillna("-")` | Used as a placeholder for categorical `Cabin`/`Embarked` |
| ➖ `fillna("")` | Used to blank out missing `Age` entries |

---

## 📊 Part B — Visualization & Insights

### 📶 4. Bar Chart — Survivors by Sex

**Logic:**
```python
Sex = df.groupby("Sex")["Survived"].sum()
plt.figure(figsize=(10,5))
plt.bar(Sex.index, Sex.values, color="skyblue")
plt.xticks(rotation=45)
plt.title("survived By Country")
plt.xlabel("Sex")
plt.ylabel("Survived")
plt.show()
```

---

### 📈 5. Line Chart — Ticket Count by Passenger Class

**Logic:**
```python
Pclass = df.groupby("Pclass")["Ticket"].sum()
plt.figure(figsize=(10,5))
plt.plot(Pclass.index, Pclass.values, marker="o", color="red")
plt.title("Ticket by Pclass")
plt.xlabel("Pclass")
plt.ylabel("Ticket")
plt.grid(True)
plt.show()
```

---

### 🥧 6. Pie Chart — Ticket Share by Sex

**Logic:**
```python
Sex = df.groupby("Sex")["Ticket"].sum()
plt.figure(figsize=(8,8))
plt.pie(Sex.values, labels=Sex.index, autopct="%1.1f%%", startangle=90)
plt.title("Ticket by Sex")
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

- ✅ **Fully Cleaned Dataset** — Age, Fare, Cabin, and Embarked free of missing values
- 🚻 **Gender Insight** — Survival counts clearly compared between male and female passengers
- 🎟️ **Class Trend** — Ticket distribution visualized across Passenger Classes
- 🥧 **Ticket Share Insight** — Gender-wise ticket proportion visualized
- 💾 **Optional Export** — Each chart can be saved as a high-resolution PNG

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Core EDA concepts: cleaning, grouping, and plotting in one notebook |
| 🔄 **Reusability** | Cleaning logic can be reused for any similar mixed-type dataset |
| 📚 **Educational** | Demonstrates real-world missing value handling across data types |
| 🖥️ **Minimal Dependencies** | Runs with standard Python data-science libraries only |
| ⚡ **Lightweight** | Single-notebook workflow, runs top-to-bottom in seconds |
| 🧪 **Extensible** | Easy to add survival prediction models (Logistic Regression, etc.) |
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

### KRINAL DHOLAKYA

[![GitHub](https://img.shields.io/badge/GitHub-krinaldholakiya-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/krinaldholakiya)

> *"Behind every row of data was a real person aboard that ship."*

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
- 🚢 [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic) — Dataset inspiration

---

<div align="center">

---

*Made with ❤️ — Last updated: 19 July, 2026*

</div>
