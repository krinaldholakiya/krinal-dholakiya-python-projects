<div align="center">

# -- ! Data Analysis & Visualization Program ! --
### *Interactive Console-Based CSV Explorer, Cleaner & Chart Generator*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-DataFrame-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![OOP](https://img.shields.io/badge/Design-OOP%20Class%20Based-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"Data doesn't speak for itself — it needs a good interface to be heard."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📂 Part A — Dataset Loading & Exploration](#-part-a--dataset-loading--exploration)
- [🧮 Part B — Dataframe Operations](#-part-b--dataframe-operations)
- [🧹 Part C — Handling Missing Data](#-part-c--handling-missing-data)
- [📊 Part D — Data Visualization](#-part-d--data-visualization)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Data Analysis & Visualization Program** is a menu-driven, object-oriented Python console application built around a single `DataAnalyzer` class. It lets a user load any CSV dataset and interactively explore, clean, summarize, and visualize it — all from a text-based menu system without touching a Jupyter cell more than once.

This project is designed to:
- Demonstrate real-world usage of **Pandas** for data loading, exploration, and cleaning
- Apply **Seaborn** and **Matplotlib** to build multiple chart types from live data
- Practice **OOP design** by encapsulating all logic inside a single reusable class
- Use Python's modern **`match-case`** syntax for clean, readable menu routing
- Handle **missing data**, **descriptive statistics**, and **data export** (saved charts)

---

## 🎯 Problem Statement

> **Objective:** Build an interactive, menu-driven console tool that loads a CSV dataset and lets the user explore, clean, summarize, and visualize it on demand.

You are building a lightweight data-analysis utility for anyone who wants to inspect a dataset without writing a new script every time. The program must accept a file path, load it into a Pandas DataFrame, and then present a hierarchy of menus for exploration, transformation, and plotting — including the option to save any generated chart to disk.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Dataset Loader | I/O | Reads any CSV file into a Pandas DataFrame |
| Data Explorer | Inspection | Head, tail, columns, dtypes, and `.info()` |
| Dataframe Operations | Analysis | Unique values, min/max discount & rating |
| Missing Data Handler | Cleaning | Detect, fill (mean / placeholder), or drop |
| Descriptive Statistics | Summary | Full `.describe()` numeric summary |
| Data Visualization | Charting | Bar, Line, Scatter, Pie, Histogram, Stack Plot |

The goal is to demonstrate **practical data-analysis and visualization skills** through a clean, menu-driven, class-based program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Main menu runs continuously until the user selects Exit |
| 📥 **Dynamic CSV Loading** | Load any dataset at runtime by supplying its file path |
| 🔍 **6-Way Data Exploration** | Head, tail, columns, dtypes, info, and a back-to-menu exit |
| 🧮 **Dataframe Insights** | Unique products/categories, discount & rating extremes |
| 🧹 **Missing Data Toolkit** | View, fill (mean/placeholder), or drop null values |
| 📊 **6 Chart Types** | Bar, Line, Scatter, Pie, Histogram, and Stack Plot via Seaborn |
| 💾 **Save-to-File Option** | Every chart can optionally be exported as a high-res PNG |
| ✅ **Input-Driven Flow** | Fully driven by user input with `match-case` branching |
| ⚠️ **Safety Checks** | Every operation checks if a dataset is loaded before running |

---

## 🏗️ Project Structure

```
📦 data-analysis-visualization/
│
├── 📄 pr-9.ipynb             ← Main Jupyter notebook (entry point)
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
│   Display Main Menu         │  ← 1-7: Load / Explore / Ops / Clean / Stats / Viz / Exit
└────────────┬────────────────┘
             │
   ┌─────────┼─────────┬─────────────┬─────────────┐
   ▼         ▼         ▼             ▼             ▼
┌────────┐ ┌────────┐ ┌───────────┐ ┌───────────┐ ┌────────────┐
│Choice:1│ │Choice:2│ │ Choice: 3 │ │ Choice: 4 │ │ Choice: 6  │
│(Load)  │ │(Explore│ │(Dataframe │ │(Missing   │ │(Visualize) │
│        │ │ Data)  │ │Operations)│ │  Data)    │ │            │
└───┬────┘ └───┬────┘ └─────┬─────┘ └─────┬─────┘ └─────┬──────┘
    │          │            │             │             │
    ▼          ▼            ▼             ▼             ▼
┌─────────────────────────────────────────────────────────────┐
│           Sub-Menu Loop → Perform Task → Show Output         │
└────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
                      Loop Back to Menu
                              │
                       (Choice: 7) Exit ✅
```

---

## 📂 Part A — Dataset Loading & Exploration

### 📝 1. Loading the Dataset

> The user supplies a CSV file path, which is read directly into a Pandas DataFrame stored as a class attribute.

**Logic:**
```python
def load_dataset(self):
    load_choice = input("Enter The Path Of The Dataset (CSV File): ")
    try:
        self.df = pd.read_csv(load_choice)
        print("Dataset Loaded Successfully!")
    except Exception as e:
        print(f"Error loading file: {e}")
```

---

### 🔍 2. Explore Data — Sub-Menu

> A dedicated sub-menu using `match-case` to route between six inspection options.

**Logic:**
```python
match case2_choice:
    case 1: print(self.df.head(5))
    case 2: print(self.df.tail(5))
    case 3: print(self.df.columns)
    case 4: print(self.df.dtypes)
    case 5: print(self.df.info())
    case 6: break
```

**Options Available:**

| Option | Action |
|--------|--------|
| 1️⃣ | Display the first 5 rows |
| 2️⃣ | Display the last 5 rows |
| 3️⃣ | Display column names |
| 4️⃣ | Display data types |
| 5️⃣ | Display basic dataset info |
| 6️⃣ | Return to main menu |

---

## 🧮 Part B — Dataframe Operations

> Extracts targeted insights from specific columns such as `Product`, `Category`, `DiscountPct`, and `CustomerRating`.

**Logic:**
```python
case 1: print(self.df["Product"].unique())
case 2: print(self.df["Category"].unique())
case 3:
    print(self.df['DiscountPct'].max())
    print(self.df['DiscountPct'].min())
case 4:
    print(self.df['CustomerRating'].max())
    print(self.df['CustomerRating'].min())
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🔠 `.unique()` | Lists all distinct product / category names |
| 📈 `.max()` / `.min()` | Finds the highest and lowest discount & rating |
| 🖨️ f-strings | Formatted, labeled console output |

---

## 🧹 Part C — Handling Missing Data

> Detects, repairs, or removes missing values across the dataset.

**Logic:**
```python
case 1:
    print(self.df.isna())
case 2:
    self.df.fillna({'UnitPrice': self.df['UnitPrice'].mean()}, inplace=True)
    self.df.fillna({'Product': "-"}, inplace=True)
    self.df.fillna({'Region': "-"}, inplace=True)
    self.df.fillna({'Quantity': self.df['Quantity'].mean()}, inplace=True)
    self.df.fillna({'DiscountPct': self.df['DiscountPct'].mean()}, inplace=True)
    self.df.fillna({'CustomerRating': self.df['CustomerRating'].mean()}, inplace=True)
case 3:
    self.df.dropna(inplace=True)
```

**Strategy Summary:**

| Column Type | Fill Strategy |
|-------------|----------------|
| 🔢 Numeric (`UnitPrice`, `Quantity`, `DiscountPct`, `CustomerRating`) | Filled with column **mean** |
| 🔤 Categorical (`Product`, `Region`) | Filled with placeholder **"-"** |
| 🧾 Row-level | Optionally dropped entirely with `.dropna()` |

---

## 📊 Part D — Data Visualization

### 🗺️ Chart Types — Overview

| Chart | Library Call | Purpose |
|-------|--------------|---------|
| 1️⃣ Bar Plot | `sns.barplot()` | Compare sales across products |
| 2️⃣ Line Plot | `sns.lineplot()` | Trend of sales per product |
| 3️⃣ Scatter Plot | `sns.scatterplot()` | Sales vs product, colored by region |
| 4️⃣ Pie Chart | `plt.pie()` | Product-wise sales share (%) |
| 5️⃣ Histogram | `sns.histplot()` | Distribution of sales values |
| 6️⃣ Stack Plot | `plt.stackplot()` | Monthly sales stacked by product |

**Sample Logic — Bar Plot:**
```python
plt.figure(figsize=(10,5))
sns.barplot(x="Product", y="Sales", data=self.df, errorbar=None)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title("Product Sales")

save = input("Do You Want To Save Graph?(yes or no): ")
if save.lower() == "yes":
    plt.savefig("barplot.png", dpi=300, bbox_inches='tight')
    print("Your Graph Saved Successfully!")
plt.show()
```

**Sample Logic — Stack Plot (Monthly Trend):**
```python
self.df['Date'] = pd.to_datetime(self.df['Date'])
self.df['Month'] = self.df['Date'].dt.to_period('M').astype(str)
df_pivot = self.df.groupby(['Month', 'Product'])['Sales'].sum().unstack().fillna(0)
plt.stackplot(df_pivot.index, df_pivot.values.T, labels=df_pivot.columns)
```

**Every chart supports:**

| Feature | Detail |
|---------|--------|
| 💾 Save-to-PNG | High-resolution (`dpi=300`) export on request |
| 🏷️ Custom Labels | Bar plot lets the user set custom X/Y axis labels |
| 🎨 Region-aware Coloring | Scatter plot uses `hue="Region"` for grouping |
| 📆 Time-Aware Grouping | Stack plot resamples data by month automatically |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core language (uses `match-case`) |
| 🐼 **Pandas** | Latest | DataFrame loading, cleaning & analysis |
| 🌊 **Seaborn** | Latest | Statistical chart styling (bar/line/scatter/hist) |
| 📐 **Matplotlib** | Latest | Core plotting engine & figure export |
| 🔂 **While Loop** | Built-in | Menu persistence and sub-menu navigation |
| 🧮 **match-case** | Python 3.10+ | Clean, readable menu routing |
| 🖨️ **print() / input()** | Built-in | Console I/O and user interaction |

---

## 📈 Results & Insights

After running the program, the following outputs are produced:

- ✅ **Interactive CSV Exploration** — first/last rows, columns, dtypes, and info at a glance
- 🧮 **Column-Level Insights** — unique products/categories, discount & rating extremes
- 🧹 **Cleaned Dataset** — missing values filled or dropped on demand
- 📊 **6 Chart Types** — Bar, Line, Scatter, Pie, Histogram, and Stack Plot
- 💾 **Exportable Graphs** — every chart can be saved as a 300-DPI PNG file
- 🔁 **Persistent Menu** — program loops back after every task until manually exited

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Practical Learning** | Combines Pandas, Seaborn, and Matplotlib in one workflow |
| 🧱 **OOP Design** | All logic encapsulated in a single `DataAnalyzer` class |
| 🔄 **Reusability** | Works with any CSV that follows a tabular structure |
| 📚 **Educational** | Each menu reinforces a distinct data-analysis concept |
| 🖥️ **No Hardcoded Data** | Fully dynamic — load and explore any dataset at runtime |
| ⚡ **Fast Feedback** | Interactive console output for every operation |
| 🧪 **Extensible** | Easy to add new plot types or statistical operations |
| 🛡️ **Guarded Operations** | Every feature checks if a dataset is loaded first |

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

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourhandle)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yourhandle/)

> *"Every dataset has a story — a good plot is how you tell it."*

**🎓 Role:** Python Developer | Data Analysis Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · Pandas · Seaborn · Matplotlib · OOP · Data Visualization

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🐼 [Pandas Documentation](https://pandas.pydata.org/docs/) — DataFrame operations & cleaning
- 🌊 [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical visualization reference
- 📐 [Matplotlib Documentation](https://matplotlib.org/stable/index.html) — Core plotting reference
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python, Pandas, and Data Visualization courses

---

<div align="center">

---

*Made with ❤️ and 📊 — Last updated: 15 July, 2026*

</div>
