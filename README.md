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
│   ├── 📓 Notebooks (start here — click to open on GitHub)
│   │   ├── netflixlast.ipynb       → https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/netflixlast.ipynb
│   │   ├── netflix.ipynb           → https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/netflix.ipynb
│   │   ├── hr.ipynb                → https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/hr.ipynb
│   │   ├── zomatowala.ipynb        → https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/zomatowala.ipynb
│   │   ├── sales.ipynb             → https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/sales.ipynb
│   │   ├── fashion.ipynb           → https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/fashion.ipynb
│   │   ├── notebook.ipynb          → https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/notebook.ipynb
│   │   ├── pyjanitor.ipynb         → https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/pyjanitor.ipynb
│   │   └── matplotlib.ipynb        → https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/matplotlib.ipynb
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

### Step 1 — 📺 Exploring Raw Data
**Notebook:** [`data_cleaning/netflix.ipynb`](https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/netflix.ipynb)  
**Dataset:** [`netflix1.csv`](https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/netflix1.csv)

| Concept | Method |
|---------|--------|
| Load a CSV | `pd.read_csv()` |
| Preview rows | `head()`, `tail()` |
| Understand the data | `.shape`, `.columns`, `.dtypes` |
| Check null counts | `isnull().sum()` |

> **Goal:** Load a CSV file and get a first look at messy real‑world data.

---

### Step 2 — 📺 Full Cleaning Pipeline
**Notebook:** [`data_cleaning/netflixlast.ipynb`](https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/netflixlast.ipynb)  
**Dataset:** [`netflix_titles.csv`](https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/netflix_titles.csv)

| Concept | Method |
|---------|--------|
| Count missing values | `isnull().sum()`, `isna().sum()` |
| Remove duplicates | `duplicated()`, `drop_duplicates()` |
| Fill missing values | `fillna()` |
| Drop rows with nulls | `dropna()` |
| Parse date strings | `pd.to_datetime()` |
| Export cleaned data | `to_excel()` |

> **Goal:** Complete end‑to‑end cleaning of a dataset — **the most important notebook in the guide**.

---

### Step 3 — 👥 Cleaning Categorical Data
**Notebook:** [`data_cleaning/hr.ipynb`](https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/hr.ipynb)  
**Dataset:** [`HR-Employee-Attrition.csv`](https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/HR-Employee-Attrition.csv)

| Concept | Method |
|---------|--------|
| Drop useless columns | `drop(columns=[...])` |
| Rename columns | `rename(columns={...})` |
| Handle categorical data | `value_counts()`, `replace()` |
| Convert types | `astype()` |
| Export cleaned CSV | `to_csv(index=False)` |

> **Goal:** Handle mixed numeric + categorical columns in real HR employee data.

---

### Step 4 — 🍽️ Advanced String Cleaning
**Notebook:** [`data_cleaning/zomatowala.ipynb`](https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/zomatowala.ipynb)  
**Dataset:** Zomato restaurant data (included in notebook)

| Concept | Method |
|---------|--------|
| Remove currency symbols | `str.replace('₹', '')` |
| Strip whitespace | `str.strip()` |
| Lowercase text | `str.lower()` |
| Count unique values | `nunique()` |
| Apply custom logic | `apply()` + `lambda` |

> **Goal:** Clean messy restaurant data across 50+ steps — the **most comprehensive** cleaning notebook.

---

### Step 5 — 💰 Missing Values & Export
**Notebook:** [`data_cleaning/sales.ipynb`](https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/sales.ipynb)  
**Dataset:** [`sales.csv`](https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/sales.csv)

| Concept | Method |
|---------|--------|
| Count total nulls | `isnull().sum().sum()` |
| Drop null rows | `dropna(inplace=True)` |
| Forward fill nulls | `fillna(method='ffill')` |
| Export to Excel | `to_excel(index=False)` |
| Export to CSV | `to_csv(index=False)` |

> **Goal:** Handle missing values in business sales data and export the cleaned version.

---

### Step 6 — 👗 Column Cleaning
**Notebook:** [`data_cleaning/fashion.ipynb`](https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/fashion.ipynb)  
**Dataset:** [`FashionDataset.csv`](https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/FashionDataset.csv)

| Concept | Method |
|---------|--------|
| Drop unnamed index column | `drop(columns='Unnamed: 0')` |
| Check missing values | `isnull().sum()` |
| Clean column names | `str.lower()`, `str.strip()` |
| Check data types | `.dtypes` |

> **Goal:** Remove unwanted columns and clean column names in e‑commerce fashion data.

---

### Step 7 — 🏠 Large Dataset Exploration
**Notebook:** [`data_cleaning/notebook.ipynb`](https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/notebook.ipynb)  
**Dataset:** [`Airbnb_Open_Data.csv`](https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/Airbnb_Open_Data.csv) (~36 MB)

| Concept | Method |
|---------|--------|
| Load a large CSV | `pd.read_csv()` |
| Preview safely | `head()` |
| Inspect columns | `.columns`, `.info()` |

> **Goal:** Understand how to explore a very large dataset without crashing your kernel.

---

### Step 8 — 🧹 Automated Cleaning with pyjanitor
**Notebook:** [`data_cleaning/pyjanitor.ipynb`](https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/pyjanitor.ipynb)  
**Dataset:** Synthetically generated HR-like data

| Concept | pyjanitor Method |
|---------|-----------------|
| Standardise column names | `clean_names()` |
| Remove empty rows/cols | `remove_empty()` |
| Rename a column | `rename_column()` |
| Filter rows | `filter_on()` |
| Expand multi-value cells | `expand_column()` |

> **Goal:** Use `pyjanitor` to clean DataFrames with beautiful one-line method chaining.

---

### Step 9 — 📊 Visualising Clean Data
**Notebook:** [`data_cleaning/matplotlib.ipynb`](https://github.com/Cy-nape/PANDAS-learning-/blob/main/data_cleaning/matplotlib.ipynb)  
**Dataset:** Custom numeric data

| Chart Type | Method |
|------------|--------|
| Line chart | `plt.plot()` |
| Bar chart | `plt.bar()` |
| Scatter plot | `plt.scatter()` |
| Histogram | `plt.hist()` |
| Customise | `color`, `marker`, `label`, `title` |

> **Goal:** Visualise clean data to find patterns — the final step of every data project.

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
