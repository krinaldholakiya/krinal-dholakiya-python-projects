<div align="center">

# -- ! COVID-19 Data Analysis & Visualization ! --
### *End-to-End Exploratory Data Analysis, Data Cleaning & Visual Storytelling*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-DataFrame-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"Data is the new oil, but visualization is the engine that turns it into insight."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 Part A — Data Loading & Exploration](#-part-a--data-loading--exploration)
- [🧼 Part B — Data Cleaning](#-part-b--data-cleaning)
- [📊 Part C — Data Visualization](#-part-c--data-visualization)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **COVID-19 Data Analysis & Visualization** project is a Jupyter Notebook–based exploratory data analysis (EDA) pipeline built with **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**. It loads a global COVID-19 dataset, inspects and cleans it, and then transforms raw numbers into clear, colourful visual stories — bar charts, line graphs, pie charts, and histograms — with an interactive option to save every plot to disk.

This project is designed to:
- Practice reading, inspecting, and summarizing real-world tabular data
- Detect and handle missing values and duplicate records
- Apply `groupby` aggregations to summarize data by country
- Build a variety of publication-ready charts using Matplotlib and Seaborn
- Provide an interactive save-to-file workflow for every generated graph

---

## 🎯 Problem Statement

> **Objective:** Analyze a large COVID-19 records dataset to understand case trends, vaccination coverage, and mortality patterns across countries.

You are given a dataset (`covid19.csv`) containing 5,000 daily country-level COVID-19 records — cases, deaths, recoveries, tests, vaccinations, hospitalizations, and ICU admissions. The task is to load the dataset, explore its structure, clean missing values, and generate meaningful visual summaries that make the numbers easy to interpret at a glance.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading | I/O | Reads `covid19.csv` into a Pandas DataFrame |
| Data Inspection | Exploration | Shape, columns, dtypes, head/tail preview |
| Missing Value Handling | Cleaning | Detects & fills nulls using mean imputation |
| Duplicate Check | Cleaning | Verifies there are no duplicate records |
| Bar Chart | Visualization | Population by Country |
| Line Chart | Visualization | Vaccinations by Country |
| Pie Chart | Visualization | Share of New Cases by Country |
| Histogram | Visualization | Distribution of records by Country |

The goal is to demonstrate a **complete, practical EDA workflow** — from raw CSV to clean, decision-ready visuals.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **CSV Ingestion** | Loads the dataset with `pandas.read_csv()` and confirms successful load |
| 🔍 **Data Preview** | `head()` and `tail()` calls to inspect first and last 10 records |
| 📐 **Shape & Schema Check** | Prints dataset shape, column names, and data types |
| 🧾 **Info Summary** | `df.info()` for a concise structural overview |
| 📊 **Statistical Summary** | `df.describe()` for mean, std, min, max, and quartiles |
| 🕳️ **Null Detection** | `isnull().sum()` to flag missing values per column |
| 🧬 **Duplicate Detection** | `duplicated().sum()` to confirm data integrity |
| 🩹 **Mean Imputation** | Fills missing values in `Recovered`, `Vaccinations`, `Hospitalized` |
| 🌍 **Country-wise Aggregation** | `groupby("Country")` for population, vaccination & case totals |
| 🎨 **Four Chart Types** | Bar, Line, Pie, and Histogram — each in a distinct colour palette |
| 💾 **Interactive Save Prompt** | Every chart asks *"Do you want to save graph (yes/no)"* before exporting as PNG |

---

## 🏗️ Project Structure

```
📦 covid19-data-analysis/
│
├── 📄 1784463898803_1.ipynb   ← Main Jupyter Notebook (entry point)
├── 📄 covid19.csv             ← Source dataset (5,000 records × 13 columns)
│
├── 🖼️ barchart.png            ← Population by Country (generated on save)
├── 🖼️ Linegraph.png           ← Vaccinations by Country (generated on save)
├── 🖼️ Piechart.png            ← New Cases share by Country (generated on save)
├── 🖼️ Histogram.png           ← Country-wise record distribution (generated on save)
│
└── 📄 README.md               ← Project documentation
```

---

## 🔄 Project Workflow

```
Notebook Start
      │
      ▼
┌─────────────────────────────┐
│   Import Libraries          │  ← numpy, pandas, seaborn, matplotlib
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Load covid19.csv          │  ← pd.read_csv()
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Explore Dataset           │  ← head/tail, shape, columns, info, describe
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Check Nulls & Duplicates  │  ← isnull().sum(), duplicated().sum()
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Clean Missing Values      │  ← fillna(mean()) on 3 numeric columns
└────────────┬────────────────┘
             │
     ┌───────┴────────────────────────┬───────────────┬───────────────┐
     ▼                                ▼               ▼               ▼
┌───────────┐                 ┌───────────┐   ┌───────────┐   ┌───────────┐
│ Bar Chart │                 │ Line Chart│   │ Pie Chart │   │ Histogram │
└─────┬─────┘                 └─────┬─────┘   └─────┬─────┘   └─────┬─────┘
      │                             │               │               │
      ▼                             ▼               ▼               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│              Prompt: Save Graph? (yes/no) → Export as PNG               │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🧹 Part A — Data Loading & Exploration

### 📝 1. Loading the Dataset

The dataset is read from a CSV file into a Pandas DataFrame, with a confirmation message printed on success.

**Logic:**
```python
df = pd.read_csv("covid19.csv")
print("dataset loaded successfull!")
```

---

### 🔍 2. Previewing the Data

`head()` and `tail()` display the first and last 10 rows, giving a quick look at the dataset's structure and value ranges.

**Logic:**
```python
df.head(10)
df.tail(10)
```

---

### 📐 3. Shape, Columns & Data Types

Understanding the dataset's dimensions and schema is the first step before any analysis.

**Logic:**
```python
print("shape of dataset:", df.shape)
print("column of dataset:", df.columns)
print(df.info())
print(df.dtypes)
```

**Sample Output:**
```
shape of dataset: (5000, 13)
```

---

### 📊 4. Statistical Summary

`describe()` returns count, mean, standard deviation, min, max, and quartile values for every numeric column — useful for spotting outliers and understanding scale.

**Logic:**
```python
print(df.describe())
```

---

## 🧼 Part B — Data Cleaning

### 🕳️ 5. Detecting Missing Values

> Three columns — `Recovered`, `Vaccinations`, and `Hospitalized` — contain 250 missing values each out of 5,000 records.

**Logic:**
```python
print(df.isnull().sum())
```

---

### 🧬 6. Checking for Duplicates

A quick duplicate check confirms the dataset has zero duplicate rows, and a date-type validation confirms all `Date` values parse correctly.

**Logic:**
```python
print(df.duplicated().sum())
print(df["Date"] == pd.to_datetime(df["Date"]))
```

---

### 🩹 7. Filling Missing Values

> Missing numeric values are imputed using the **column mean**, a simple and effective strategy for continuous data.

**Logic:**
```python
df["Recovered"] = df["Recovered"].fillna(df["Recovered"].mean())
df["Vaccinations"] = df["Vaccinations"].fillna(df["Vaccinations"].mean())
df["Hospitalized"] = df["Hospitalized"].fillna(df["Hospitalized"].mean())
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🕳️ `isnull().sum()` | Counts missing values per column |
| 🩹 `fillna(mean())` | Mean imputation for numeric columns |
| 🧬 `duplicated().sum()` | Confirms row-level data integrity |
| 🗓️ `pd.to_datetime()` | Validates date column formatting |

---

## 📊 Part C — Data Visualization

### 🟦 8. Bar Chart — Population by Country

> Aggregates total population per country using `groupby().sum()` and renders it as a sky-blue bar chart.

**Logic:**
```python
country = df.groupby("Country")["Population"].sum()
plt.figure(figsize=(10, 5))
plt.bar(country.index, country.values, color="skyblue")
plt.xticks(rotation=45)
plt.title("Population By Country")
plt.xlabel("Country")
plt.ylabel("Population")
```

---

### 🔴 9. Line Chart — Vaccinations by Country

> Plots total vaccinations per country as a red line with circular markers and a grid for easy reading.

**Logic:**
```python
Country = df.groupby("Country")["Vaccinations"].sum()
plt.figure(figsize=(10, 5))
plt.plot(Country.index, Country.values, marker="o", color="red")
plt.title("Vaccination by Country")
plt.xlabel("Country")
plt.ylabel("Vaccinations")
plt.grid(True)
```

---

### 🥧 10. Pie Chart — New Cases Share by Country

> Visualizes each country's percentage share of total new cases using an exploded-style pie chart with percentage labels.

**Logic:**
```python
Country = df.groupby("Country")["New_Cases"].sum()
plt.figure(figsize=(8, 8))
plt.pie(Country.values, labels=Country.index, autopct="%1.1f%%", startangle=90)
plt.title("New Cases by Country")
```

---

### 🟣 11. Histogram — Record Distribution by Country

> Uses Seaborn's `histplot()` to show how many records exist per country in a bold purple palette.

**Logic:**
```python
plt.figure(figsize=(12, 5))
sns.histplot(data=df, x="Country", color="purple")
plt.xticks(rotation=45)
plt.xlabel("Country")
plt.ylabel("New_Death")
plt.title("New Death by Country")
```

---

### 💾 12. Interactive Save Prompt

> Every chart in the notebook ends with an interactive prompt so the user can choose whether to export the figure as a high-resolution PNG (300 DPI).

**Logic:**
```python
save = input("Do you want to save graph (yes/no): ")
if save.lower() == "yes":
    plt.savefig("barchart.png", dpi=300, bbox_inches="tight")
    print("Graph Saved Successfully!")
plt.show()
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🎨 `plt.figure(figsize=...)` | Controls chart canvas size |
| 🌈 Custom Colours | `skyblue`, `red`, `purple` for visual distinction |
| 🔁 `groupby().sum()` | Country-wise aggregation before plotting |
| 💾 `plt.savefig(dpi=300)` | High-resolution export on user confirmation |
| 🖨️ `input()` | Interactive yes/no save workflow per chart |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🐼 **Pandas** | Latest | Data loading, cleaning & aggregation |
| 🔢 **NumPy** | Latest | Numerical operations support |
| 📊 **Matplotlib** | Latest | Bar, line & pie chart plotting |
| 🎨 **Seaborn** | Latest | Statistical histogram visualization |
| 📓 **Jupyter Notebook** | Latest | Interactive development environment |
| 🖨️ **input() / print()** | Built-in | Interactive save prompts & console output |

---

## 📈 Results & Insights

After running the notebook, the following outputs are produced:

- ✅ **Clean Dataset** — All 750 missing values (250 each in 3 columns) filled via mean imputation
- 🧬 **Zero Duplicates** — Confirmed integrity across all 5,000 records
- 🌍 **10 Countries Analyzed** — UK, Japan, Germany, Canada, Brazil, France, Australia, India, USA, Italy
- 📊 **4 Distinct Visualizations** — Bar, Line, Pie, and Histogram, each highlighting a different metric
- 💾 **On-Demand PNG Exports** — High-resolution (300 DPI) charts saved only when requested

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Covers the full EDA lifecycle: load → explore → clean → visualize |
| 🔄 **Reusable Pipeline** | Cleaning and plotting logic can be adapted to any similar CSV dataset |
| 📚 **Educational** | Demonstrates real-world use of Pandas `groupby`, `fillna`, and `describe` |
| 🖥️ **Minimal Dependencies** | Runs with standard data-science libraries — no exotic packages needed |
| ⚡ **Interactive** | User controls whether each chart is saved, avoiding clutter |
| 🧪 **Extensible** | Easy to add new chart types (box plots, heatmaps, correlation matrices) |
| 📖 **Readable Code** | Clear, linear notebook structure that's easy to follow cell by cell |
| 🛡️ **Data Integrity Checks** | Explicit null and duplicate validation before any analysis |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Your Name Here

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)

> *"Behind every great visualization is a well-cleaned dataset."*

**🎓 Role:** Data Analyst | Python Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · Pandas · NumPy · Matplotlib · Seaborn · Data Cleaning · EDA

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Pandas Official Docs](https://pandas.pydata.org/docs/) — Official Pandas library reference
- 📊 [Matplotlib Documentation](https://matplotlib.org/stable/index.html) — Plotting and visualization reference
- 🎨 [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical visualization guide
- 🔢 [NumPy Official Docs](https://numpy.org/doc/) — Numerical computing reference
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Data analysis and visualization courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 19 July, 2026*

</div>
