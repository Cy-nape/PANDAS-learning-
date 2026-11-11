# 🐼 Pandas Data Cleaning — Complete Learning Guide

> A hands‑on, beginner‑friendly learning resource focused entirely on **data cleaning with pandas**.  
> Every notebook is annotated with markdown explanations so you understand *why* each step is done — not just *what* the code does.

---

## 🎯 What This Guide Is About

Data cleaning is the most important skill in data analysis.  
Before you can draw any insight from data, you must handle:

| Problem | Pandas Solution |
|---------|----------------|
| Missing / null values | `dropna()`, `fillna()`, `isnull()` |
| Duplicate rows | `duplicated()`, `drop_duplicates()` |
| Wrong data types | `astype()`, `pd.to_datetime()` |
| Messy column names | `rename()`, `str.lower()`, `str.strip()` |
| Unwanted columns | `drop()` |
| Inconsistent strings | `str.replace()`, `str.strip()`, `str.upper()` |
| Exporting clean data | `to_csv()`, `to_excel()` |

This guide teaches every one of those through **5 real‑world datasets**:

| Dataset | File | Domain |
|---------|------|--------|
| Netflix titles | `netflix_titles.csv`, `netflix1.csv` | Entertainment |
| HR Employee Attrition | `HR-Employee-Attrition.csv` | Human Resources |
| Zomato restaurants | `zomato.csv` | Food & Hospitality |
| Sales data | `sales.csv` | Business / Retail |
| Fashion products | `FashionDataset.csv` | E‑Commerce |
| Airbnb listings | `Airbnb_Open_Data.csv` | Real Estate |

---

## 📂 Repository Structure

```
PANDAS-learning-/
│
├── data_cleaning/                  ← ⭐ Main learning folder
│   │
│   ├── 📓 Notebooks (start here)
│   │   ├── netflixlast.ipynb       # 1. Netflix — full cleaning pipeline
│   │   ├── netflix.ipynb           # 2. Netflix — exploring raw data
│   │   ├── hr.ipynb                # 3. HR Employee Attrition — cleaning
│   │   ├── zomatowala.ipynb        # 4. Zomato restaurants — advanced cleaning
│   │   ├── sales.ipynb             # 5. Sales data — missing values & export
│   │   ├── fashion.ipynb           # 6. Fashion dataset — column cleaning
│   │   ├── notebook.ipynb          # 7. Airbnb — exploring a large dataset
│   │   ├── pyjanitor.ipynb         # 8. pyjanitor — automated cleaning library
│   │   └── matplotlib.ipynb        # 9. Matplotlib — visualising clean data
│   │
│   └── 📁 Datasets
│       ├── netflix_titles.csv       # Raw Netflix data
│       ├── netflix1.csv             # Another Netflix version
│       ├── HR-Employee-Attrition.csv
│       ├── FashionDataset.csv
│       ├── Airbnb_Open_Data.csv
│       ├── sales.csv / sales.xlsx
│       ├── Cleaned_zomato_data.csv  # Final cleaned Zomato output
│       ├── cleaned_hr_data.csv      # Final cleaned HR output
│       └── exelof_last_netflix.xlsx # Final cleaned Netflix Excel output
│
├── dataframe.ipynb                 # Bonus: DataFrame fundamentals
├── series.ipynb                    # Bonus: Series fundamentals
├── missingdata.ipynb               # Bonus: Dedicated missing‑data notebook
├── GroupByAggregation.ipynb        # Bonus: GroupBy & aggregation
├── PivotTables.ipynb               # Bonus: Pivot tables
├── MERGEJOINCON.ipynb              # Bonus: Merge / Join / Concat
│
├── requirements.txt
├── CONTRIBUTING.md
└── README.md                       ← You are here
```

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/Cy-nape/PANDAS-learning-.git
cd PANDAS-learning-

# 2. Set up environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Launch Jupyter
jupyter lab
# Then open data_cleaning/ and start with netflixlast.ipynb
```

---

## 📚 Learning Path — Data Cleaning

Follow these notebooks **in order**. Each one builds on the previous.

### Step 1 — `netflix.ipynb` &nbsp;📺 Exploring Raw Data
> **Dataset:** `netflix1.csv`  
> **Concepts:** `read_csv()`, `head()`, `tail()`, `shape`, `columns`, `dtypes`, `info()`  
> **Goal:** Learn how to load a CSV file and get a first look at messy real‑world data.

---

### Step 2 — `netflixlast.ipynb` &nbsp;📺 Full Cleaning Pipeline
> **Dataset:** `netflix_titles.csv`  
> **Concepts:** `isnull()`, `isna().sum()`, `dropna()`, `fillna()`, `duplicated()`, `drop_duplicates()`, `to_datetime()`, export to Excel  
> **Goal:** Complete end‑to‑end cleaning of a dataset — the most important notebook in the guide.

---

### Step 3 — `hr.ipynb` &nbsp;👥 Cleaning Categorical Data
> **Dataset:** `HR-Employee-Attrition.csv`  
> **Concepts:** `drop()`, `rename()`, `astype()`, `value_counts()`, `replace()`, export to CSV  
> **Goal:** Handle mixed numeric + categorical columns; understand employee attrition data.

---

### Step 4 — `zomatowala.ipynb` &nbsp;🍽️ Advanced String Cleaning
> **Dataset:** `zomato.csv`  
> **Concepts:** `str.strip()`, `str.replace()`, `str.lower()`, `str.contains()`, `nunique()`, `apply()`, `lambda`  
> **Goal:** Clean messy restaurant data with 51 steps — the most comprehensive cleaning notebook.

---

### Step 5 — `sales.ipynb` &nbsp;💰 Missing Values & Export
> **Dataset:** `sales.csv`  
> **Concepts:** `dropna()`, `fillna(method='ffill')`, `isnull()`, `to_excel()`, `to_csv()`  
> **Goal:** Handle missing values in business data and export the clean version.

---

### Step 6 — `fashion.ipynb` &nbsp;👗 Column Cleaning
> **Dataset:** `FashionDataset.csv`  
> **Concepts:** `drop(columns=...)`, `rename()`, `str.lower()`, `str.strip()`, handling unnamed columns  
> **Goal:** Remove unwanted columns and clean column names in e‑commerce data.

---

### Step 7 — `notebook.ipynb` &nbsp;🏠 Large Dataset Exploration
> **Dataset:** `Airbnb_Open_Data.csv` (~36 MB)  
> **Concepts:** `head()`, `info()`, `columns`, memory‑efficient reading  
> **Goal:** Understand how to explore a very large dataset without crashing the kernel.

---

### Step 8 — `pyjanitor.ipynb` &nbsp;🧹 Automated Cleaning with pyjanitor
> **Dataset:** Synthetic HR data  
> **Concepts:** `clean_names()`, `remove_empty()`, `rename_column()`, `filter_on()`, `expand_column()`  
> **Goal:** Use the `pyjanitor` library to clean DataFrames with method chaining in one line.

---

### Step 9 — `matplotlib.ipynb` &nbsp;📊 Visualising Clean Data
> **Concepts:** `plt.plot()`, `plt.bar()`, `plt.scatter()`, `plt.hist()`, customising charts  
> **Goal:** After cleaning, visualise the data to find patterns and insights.

---

## 🧠 Key Pandas Concepts at a Glance

```python
import pandas as pd

df = pd.read_csv("data.csv")       # Load data

# --- Exploration ---
df.head()                          # First 5 rows
df.info()                          # Columns, types, non-null counts
df.describe()                      # Summary statistics
df.shape                           # (rows, columns)
df.dtypes                          # Data type of each column
df.columns                         # List all column names

# --- Missing Values ---
df.isnull().sum()                  # Count nulls per column
df.dropna()                        # Drop rows with any null
df.fillna(0)                       # Fill nulls with 0
df.fillna(method='ffill')          # Forward fill

# --- Duplicates ---
df.duplicated().sum()              # Count duplicate rows
df.drop_duplicates(inplace=True)   # Remove duplicates

# --- Columns ---
df.drop(columns=['col1','col2'])   # Remove columns
df.rename(columns={'old':'new'})   # Rename columns
df.columns = df.columns.str.lower().str.strip()  # Clean all names

# --- Types ---
df['col'] = df['col'].astype(int)             # Convert to int
df['date'] = pd.to_datetime(df['date'])       # Parse dates

# --- String Cleaning ---
df['col'] = df['col'].str.strip()             # Remove whitespace
df['col'] = df['col'].str.lower()             # Lowercase
df['col'] = df['col'].str.replace('₹','')     # Remove symbol

# --- Export ---
df.to_csv("cleaned.csv", index=False)
df.to_excel("cleaned.xlsx", index=False)
```

---

## 📦 Requirements

```
pandas>=2.0
numpy>=1.26
jupyterlab>=4.0
matplotlib>=3.9
seaborn>=0.13
openpyxl>=3.1      # for Excel export
pyjanitor>=0.28    # for pyjanitor.ipynb only
```

Install everything:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.  
PRs that add new datasets, improve explanations, or fix bugs are always welcome!

---

## 📄 License

MIT License — feel free to use, share, and adapt this guide.

---

*Made with ❤️ for pandas learners. Happy cleaning! 🧹*
