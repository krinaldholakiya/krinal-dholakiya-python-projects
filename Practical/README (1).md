<div align="center">

# 💰 Expense Tracker Analyzer

### 📊 A Python-based Personal Expense Analysis & Visualization Tool

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)

</div>

---

## 📖 About The Project

**Expense Tracker Analyzer** is an object-oriented Python project built inside a Jupyter Notebook that lets you **load, clean, analyze, and visualize** personal expense data from a CSV file. It uses **incremental class extension** (each feature is added as a separate `class ExpenseTracker(ExpenseTracker)` block) to progressively build up a full-featured expense analysis tool.

> 🧠 Perfect for practicing **Pandas, NumPy, Matplotlib, and Seaborn** together in one real-world mini project!

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 📥 | **Data Loading** | Reads expense data from a CSV file into a Pandas DataFrame |
| 🔍 | **Dataset Info** | Displays shape, structure, and head/tail rows of the dataset |
| 🧹 | **Missing Value Handling** | Fills missing values intelligently (mean/median/placeholder) |
| 🗑️ | **Duplicate Removal** | Detects and removes duplicate records |
| 📈 | **Statistical Summary** | Generates descriptive statistics and unique category listings |
| 🔢 | **NumPy Analysis** | Computes total, average, min, max, median & std. deviation of expenses |
| 🗂️ | **Group Analysis** | Aggregates expenses by category and payment method |
| 📊 | **Bar Chart** | Visualizes expense distribution by category |
| 📉 | **Line Chart** | Shows monthly expense trends over time |
| 🥧 | **Pie Chart** | Displays percentage-wise expense distribution |
| 📶 | **Histogram** | Shows merchant-wise transaction frequency |
| 💾 | **Save Graphs** | Option to save any chart as a high-resolution PNG image |

---

## 🗂️ Project Structure

```
📦 Expense-Tracker-Analyzer
 ┣ 📜 practical.ipynb        # Main Jupyter Notebook with all code
 ┣ 📜 dataset.csv            # Input expense dataset (CSV)
 ┣ 🖼️ barchart.png           # Saved bar chart (generated on demand)
 ┣ 🖼️ Linegraph.png          # Saved line chart (generated on demand)
 ┣ 🖼️ Piechart.png           # Saved pie chart (generated on demand)
 ┣ 🖼️ Histogram.png          # Saved histogram (generated on demand)
 ┗ 📜 README.md              # Project documentation (this file)
```

---

## 🧰 Tech Stack

- 🐍 **Python 3.9+**
- 🐼 **Pandas** — Data loading, cleaning & aggregation
- 🔢 **NumPy** — Numerical statistical analysis
- 📊 **Matplotlib** — Bar, line & pie chart visualizations
- 🌊 **Seaborn** — Histogram / distribution plots
- 📓 **Jupyter Notebook** — Interactive development environment

---

## ⚙️ Installation & Setup

### 1️⃣ Clone or Download the Project
```bash
git clone https://github.com/your-username/expense-tracker-analyzer.git
cd expense-tracker-analyzer
```

### 2️⃣ Install Required Libraries
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### 3️⃣ Add Your Dataset
Place your `dataset.csv` file in the project folder. It should contain the following columns:

| Column | Type | Description |
|--------|------|--------------|
| `Date` | date | Transaction date |
| `Amount` | float | Expense amount |
| `Quantity` | int | Quantity of items purchased |
| `Category` | string | Expense category (Food, Travel, etc.) |
| `PaymentMethod` | string | Mode of payment (Cash, Card, UPI, etc.) |
| `Merchant` | string | Merchant/store name |
| `Description` | string | Transaction description |
| `MonthlyBudget` | float | Allocated monthly budget |

### 4️⃣ Launch Jupyter Notebook
```bash
jupyter notebook practical.ipynb
```

---

## ▶️ Usage

```python
# Create an object of ExpenseTracker with your CSV file
tracker = ExpenseTracker("dataset.csv")

# Load the dataset
tracker.load_data()

# View dataset information
tracker.dataset_info()

# Clean missing values
tracker.handle_missing_values()

# Remove duplicate rows
tracker.remove_duplicates()

# Get statistical summary
tracker.summary()

# Perform NumPy-based analysis
tracker.numpy_analysis()

# Group-wise analysis (category & payment method)
tracker.group_analysis()

# Visualizations 📊
tracker.bar_graph()      # Expense by Category
tracker.line_graph()     # Monthly Expense Trend
tracker.pie_chart()      # Expense Distribution (%)
tracker.histogram()      # Merchant-wise Distribution
```

> 💡 Each graph function asks: `Do you want to save graph (yes/no):` — type `yes` to export a high-resolution PNG.

---

## 📊 Sample Visualizations

| Chart Type | Purpose |
|------------|---------|
| 📊 Bar Graph | Compare total expenses across categories |
| 📉 Line Graph | Track how expenses change month-to-month |
| 🥧 Pie Chart | See percentage share of each category |
| 📶 Histogram | Understand merchant transaction frequency |

---

## 🧩 Class Method Reference

| Method | Purpose |
|--------|---------|
| `__init__(filename)` | Initializes tracker with the dataset filename |
| `load_data()` | Loads CSV into a DataFrame |
| `dataset_info()` | Prints shape, info, head & tail |
| `handle_missing_values()` | Fills nulls in Amount, Quantity, MonthlyBudget, Merchant, Description |
| `remove_duplicates()` | Drops duplicate rows |
| `summary()` | Prints describe(), unique categories & payment methods |
| `numpy_analysis()` | Total, mean, max, min, median, std of expenses |
| `group_analysis()` | Category-wise & payment-method-wise totals |
| `bar_graph()` | Bar chart of expense by category |
| `line_graph()` | Line chart of monthly expense trend |
| `pie_chart()` | Pie chart of expense distribution |
| `histogram()` | Seaborn histogram of merchant frequency |

---

## 🚀 Future Enhancements

- [ ] Add budget vs. actual expense comparison
- [ ] Export analysis report as PDF
- [ ] Build an interactive dashboard (Streamlit/Plotly)
- [ ] Add category-wise budget alerts

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](../../issues) or open a pull request. 🙌

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use and modify it for learning purposes.

---

<div align="center">

### 🌟 If you found this project useful, don't forget to give it a star! 🌟

Made with ❤️ using Python 🐍

</div>
