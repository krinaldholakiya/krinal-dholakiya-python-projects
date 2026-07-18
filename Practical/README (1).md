<div align="center">

# -- ! Expense Tracker & Data Analyzer ! --
### *Object-Oriented Expense Data Cleaning, Statistical Analysis & Visualization*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge)](https://seaborn.pydata.org/)

<br/>

> *"Data doesn't speak for itself — clean it, analyze it, and let the charts tell the story."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 Part A — Data Loading, Cleaning & Analysis](#-part-a--data-loading-cleaning--analysis)
- [📊 Part B — Visualization & Charting](#-part-b--visualization--charting)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Expense Tracker & Data Analyzer** is an object-oriented Python project (built inside a Jupyter Notebook) that demonstrates core data-analysis concepts such as **class-based incremental design**, **data cleaning**, **NumPy statistical computation**, **Pandas group-by aggregation**, and **Matplotlib/Seaborn visualization**. The entire tool is built around a single `ExpenseTracker` class that is progressively extended, method by method, to load, clean, analyze, and visualize a personal expense dataset.

This project is designed to:
- Strengthen understanding of **class inheritance** (`class ExpenseTracker(ExpenseTracker)` pattern extension)
- Practice **data cleaning** — missing values and duplicate handling with Pandas
- Apply **NumPy** for statistical computation (mean, median, std, min, max)
- Build **group-wise aggregations** using `groupby()`
- Create **four types of visualizations** (bar, line, pie, histogram) with optional PNG export

---

## 🎯 Problem Statement

> **Objective:** Build a Python tool to load, clean, analyze, and visually summarize personal expense data from a CSV file.

You are building a personal finance utility for anyone tracking daily expenses. The program must load a CSV of transactions, clean missing/duplicate records, compute descriptive and NumPy-based statistics, group expenses by category and payment method, and render multiple chart types to visualize spending patterns.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loader | I/O | Reads CSV expense data into a DataFrame |
| Data Cleaner | Preprocessing | Handles missing values & removes duplicates |
| Statistical Summary | Analysis | Descriptive stats + unique category/payment listings |
| NumPy Analyzer | Analysis | Total, mean, median, std, min, max of expenses |
| Group Analyzer | Aggregation | Category-wise and payment-method-wise totals |
| Chart Generator | Visualization | Bar, Line, Pie & Histogram plots |

The goal is to demonstrate **practical data-analysis skills** through a clean, class-based, reusable Python tool.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🏗️ **Incremental Class Design** | Each capability is added via `class ExpenseTracker(ExpenseTracker)` extension |
| 📥 **CSV Data Loading** | Loads expense dataset into a Pandas DataFrame with confirmation message |
| 🔍 **Dataset Inspection** | Shows shape, `.info()`, and head/tail rows |
| 🧹 **Missing Value Handling** | Fills numeric columns with mean/median, text columns with placeholders |
| 🗑️ **Duplicate Removal** | Detects and drops duplicate rows, printing before/after shape |
| 📈 **Statistical Summary** | `.describe()` plus unique `Category` and `PaymentMethod` values |
| 🔢 **NumPy Analysis** | Total, average, max, min, median & standard deviation of expenses |
| 🗂️ **Group Analysis** | Category-wise and payment-method-wise expense totals, sorted top categories |
| 📊 **Bar Chart** | Expense by category with optional PNG export |
| 📉 **Line Chart** | Monthly expense trend using parsed `Date` column |
| 🥧 **Pie Chart** | Percentage-wise expense distribution by category |
| 📶 **Histogram** | Merchant-wise transaction frequency (Seaborn) |
| 💾 **Save-on-Demand** | Every chart function asks the user before saving as a high-res PNG |

---

## 🏗️ Project Structure

```
📦 expense-tracker-analyzer/
│
├── 📄 practical.ipynb        ← Main Jupyter Notebook (entry point)
├── 📄 dataset.csv            ← Input expense dataset (CSV)
├── 🖼️ barchart.png           ← Saved bar chart (generated on demand)
├── 🖼️ Linegraph.png          ← Saved line chart (generated on demand)
├── 🖼️ Piechart.png           ← Saved pie chart (generated on demand)
├── 🖼️ Histogram.png          ← Saved histogram (generated on demand)
│
└── 📄 README.md              ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│   tracker = ExpenseTracker() │  ← Initialize with CSV filename
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   load_data()                │  ← Read CSV into DataFrame
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   dataset_info()             │  ← Shape, info(), head & tail
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   handle_missing_values()    │  ← Fill nulls (mean/median/placeholder)
│   remove_duplicates()        │  ← Drop duplicate rows
└────────────┬────────────────┘
             │
     ┌───────┴────────┐
     ▼                ▼
┌─────────────┐   ┌──────────────────┐
│  summary()  │   │ numpy_analysis() │
│  group_     │   │                  │
│  analysis() │   │                  │
└──────┬──────┘   └────────┬─────────┘
       │                   │
       └─────────┬─────────┘
                  ▼
┌─────────────────────────────┐
│  bar_graph() / line_graph()  │
│  pie_chart() / histogram()   │  ← Visualize + optional save
└────────────┬────────────────┘
             │
             ▼
        Program End ✅
```

---

## 🧹 Part A — Data Loading, Cleaning & Analysis

### 📝 1. What is the `ExpenseTracker` Class?

`ExpenseTracker` is built using **incremental class extension** — each new capability is added by re-declaring `class ExpenseTracker(ExpenseTracker):` and defining one new method at a time. This keeps every stage of the pipeline isolated and easy to trace.

```python
class ExpenseTracker:
    def __init__(self, filename):
        self.filename = filename
        self.df = None
```

---

### 🗺️ 2. Core Methods — Overview

| Method | Purpose | Technique Used |
|--------|---------|-----------------|
| 1️⃣ | `load_data()` | `pd.read_csv()` to load the DataFrame |
| 2️⃣ | `dataset_info()` | `.shape`, `.info()`, `.head()`, `.tail()` |
| 3️⃣ | `handle_missing_values()` | `.fillna()` with mean/median/placeholder |
| 4️⃣ | `remove_duplicates()` | `.drop_duplicates()` |
| 5️⃣ | `summary()` | `.describe()` + `.unique()` |
| 6️⃣ | `numpy_analysis()` | `np.sum`, `np.mean`, `np.max`, `np.min`, `np.median`, `np.std` |
| 7️⃣ | `group_analysis()` | `.groupby()` on Category & PaymentMethod |

---

### 📥 3. Load & Inspect Data

> Loads the CSV file into a DataFrame and displays a confirmation with a preview.

**Logic:**
```python
class ExpenseTracker(ExpenseTracker):

    def load_data(self):
        self.df = pd.read_csv(self.filename)
        print("Dataset Loaded Successfully")
        display(self.df.head())
```

**Sample Output:**
```
Dataset Loaded Successfully
   Date        Amount   Quantity   Category   PaymentMethod   Merchant   Description
0  2026-01-02  450.0    2          Food       UPI             Zomato     Lunch order
1  2026-01-05  1200.0   1          Travel     Card            Uber       Cab ride
...
```

---

### 🧹 4. Handle Missing Values & Duplicates

> Numeric columns are filled with mean/median, text columns with placeholders, and duplicate rows are dropped.

**Logic:**
```python
class ExpenseTracker(ExpenseTracker):

    def handle_missing_values(self):
        self.df["Amount"] = self.df["Amount"].fillna(self.df["Amount"].mean())
        self.df["Quantity"] = self.df["Quantity"].fillna(self.df["Quantity"].median())
        self.df["MonthlyBudget"] = self.df["MonthlyBudget"].fillna(self.df["MonthlyBudget"].median())
        self.df["Merchant"] = self.df["Merchant"].fillna("Unknown")
        self.df["Description"] = self.df["Description"].fillna("No Description")
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🧮 Mean Imputation | `Amount` filled using column mean |
| 🎯 Median Imputation | `Quantity` & `MonthlyBudget` filled using median |
| 🏷️ Placeholder Fill | `Merchant` → `"Unknown"`, `Description` → `"No Description"` |
| 🗑️ `drop_duplicates()` | Removes exact duplicate rows in-place |

---

### 🔢 5. NumPy Statistical Analysis

> Converts the `Amount` column into a NumPy array and computes core statistics.

**Logic:**
```python
class ExpenseTracker(ExpenseTracker):

    def numpy_analysis(self):
        amount = np.array(self.df["Amount"])
        print("Total Expense :", np.sum(amount))
        print("Average Expense :", np.mean(amount))
        print("Maximum Expense :", np.max(amount))
        print("Minimum Expense :", np.min(amount))
        print("Median Expense :", np.median(amount))
        print("Standard Deviation :", np.std(amount))
```

**Sample Output:**
```
Total Expense : 48520.0
Average Expense : 970.4
Maximum Expense : 5200.0
Minimum Expense : 50.0
Median Expense : 820.0
Standard Deviation : 645.72
```

---

## 📊 Part B — Visualization & Charting

### 🔍 6. Group-wise Aggregation

> Groups total expense by `Category` and `PaymentMethod`, then ranks top spending categories.

**Logic:**
```python
class ExpenseTracker(ExpenseTracker):

    def group_analysis(self):
        category_total = self.df.groupby("Category")["Amount"].sum()
        payment = self.df.groupby("PaymentMethod")["Amount"].sum()
        top = category_total.sort_values(ascending=False)
```

---

### 📊 7. Bar Chart — Expense by Category

**Logic:**
```python
plt.bar(category.index, category.values, color="skyblue")
plt.xticks(rotation=45)
plt.title("Expense By Category")
```

### 📉 8. Line Chart — Monthly Expense Trend

**Logic:**
```python
self.df["Month"] = self.df["Date"].dt.month
monthly = self.df.groupby("Month")["Amount"].sum()
plt.plot(monthly.index, monthly.values, marker="o", color="red")
```

### 🥧 9. Pie Chart — Expense Distribution

**Logic:**
```python
plt.pie(category.values, labels=category.index, autopct="%1.1f%%", startangle=90)
```

### 📶 10. Histogram — Merchant Frequency

**Logic:**
```python
sns.histplot(data=self.df, x="Merchant", color="purple")
plt.xticks(rotation=45)
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🎨 `plt.bar()` / `plt.plot()` / `plt.pie()` | Core Matplotlib chart types |
| 🌊 `sns.histplot()` | Seaborn distribution plot |
| 💾 `input()` prompt | Asks user whether to save chart as PNG |
| 🖼️ `plt.savefig(dpi=300)` | Exports high-resolution chart images |

**Sample Interaction:**
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
| 🔢 **NumPy** | Latest | Numerical statistical analysis |
| 📊 **Matplotlib** | Latest | Bar, line & pie chart visualizations |
| 🌊 **Seaborn** | Latest | Histogram / distribution plots |
| 📓 **Jupyter Notebook** | Latest | Interactive development environment |

---

## 📈 Results & Insights

After running the notebook end-to-end, the following outputs are produced:

- ✅ **Cleaned Dataset** — No missing values, no duplicate transactions
- 🔢 **Full Statistical Profile** — Total, average, min, max, median & std. deviation of expenses
- 🗂️ **Category & Payment Breakdown** — Ranked totals by category and payment method
- 📊 **4 Chart Types** — Bar, Line, Pie, and Histogram, each optionally exportable as PNG
- 💾 **On-Demand Exports** — `barchart.png`, `Linegraph.png`, `Piechart.png`, `Histogram.png`

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Combines Pandas, NumPy, Matplotlib & Seaborn in one project |
| 🏗️ **Modular Class Design** | Each method can be extended or overridden independently |
| 📚 **Educational** | Reinforces data cleaning, aggregation & visualization workflows |
| 🖥️ **Minimal Dependencies** | Runs with standard PyData stack — no external services needed |
| ⚡ **Lightweight** | Single-notebook project, runnable instantly in Jupyter |
| 🧪 **Extensible** | Easy to add new charts (heatmaps, budget-vs-actual, etc.) |
| 📖 **Readable Code** | Clear, single-responsibility methods make logic easy to follow |
| 🛡️ **Robust Cleaning** | Handles missing values and duplicates before any analysis |

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

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/your-username)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/your-profile/)

> *"Numbers tell you what happened — visualization tells you why it matters."*

**🎓 Role:** Junior Python Developer | Data Analysis Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · Pandas · NumPy · Matplotlib · Seaborn · Data Cleaning

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🐼 [Pandas Documentation](https://pandas.pydata.org/docs/) — DataFrame operations & guides
- 🔢 [NumPy Documentation](https://numpy.org/doc/) — Numerical computing reference
- 📊 [Matplotlib Docs](https://matplotlib.org/stable/index.html) — Visualization guides
- 🌊 [Seaborn Docs](https://seaborn.pydata.org/) — Statistical plotting reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and data analysis courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 18 July, 2026*

</div>
