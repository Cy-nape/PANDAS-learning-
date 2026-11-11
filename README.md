# Pandas Learning Guide

A curated collection of Jupyter notebooks that walk you through the essential features of **pandas**, the Python data‑analysis library.  This repository is designed as a **self‑contained learning path** for beginners and intermediate users – you can clone it, set up the environment, and follow the notebooks in order.

---

## 🎯 Goal

- Understand how to create, manipulate, and analyze tabular data with pandas.
- Learn common operations: loading data, cleaning, missing‑value handling, grouping, aggregation, pivot tables, and visualisation.
- Practice on real‑world datasets (Airbnb, Zomato, Netflix, HR, Fashion, etc.) that are already included in the repo.

---

## 🛠️ Prerequisites

- **Python 3.14** (or any recent 3.x version) 
- **git**
- The repository ships a ready‑to‑use virtual environment located in `myenv`.  If you prefer a fresh environment, see the **Requirements** section below.

---

## 📂 Repository structure

```
PANDAS/
├─ data_cleaning/          # assorted cleaning & visualisation notebooks
├─ airbnb/                # Airbnb dataset analysis
├─ myenv/                 # virtual environment (optional)
├─ *.ipynb                # core learning notebooks
├─ requirements.txt       # pip requirements for a clean env
├─ README.md               # **this file**
└─ CONTRIBUTING.md        # guidelines for contributions
```

| Notebook | Topic |
|----------|-------|
| `dataframe.ipynb` | Basic DataFrame creation, indexing, and simple operations |
| `missingdata.ipynb` | Detecting, visualising, and imputing missing values |
| `GroupByAggregation.ipynb` | Group‑by patterns, custom aggregation functions |
| `PivotTables.ipynb` | Pivot tables, reshaping data |
| `airbnb/notebook.ipynb` | End‑to‑end analysis of a real Airbnb CSV dataset |
| `data_cleaning/*.ipynb` | Various cleaning, merging, and visualisation examples |
| `myenv/...` | Pre‑installed virtual environment (you can ignore it) |

---

## 🚀 Quick‑start guide

```bash
# 1️⃣ Clone the repo (or pull the latest changes)
git clone https://github.com/Cy-nape/PANDAS-learning-.git
cd PANDAS-learning-

# 2️⃣ Create a fresh conda environment (optional but recommended)
conda env create -f environment.yml   # if you add this file later
# or using pip:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3️⃣ Launch Jupyter Notebook / JupyterLab
jupyter notebook   # or `jupyter lab`
```

Open `dataframe.ipynb` first and follow the **Learning Path** outlined below.

---

## 📚 Suggested learning path

1. **`dataframe.ipynb`** – Fundamentals of pandas: Series, DataFrames, reading CSV/Excel, basic indexing.
2. **`missingdata.ipynb`** – Identify missing values, fill, drop, interpolation.
3. **`GroupByAggregation.ipynb`** – Powerful group‑by, aggregation, `apply`.
4. **`PivotTables.ipynb`** – Reshape data with `pivot_table` and `melt`.
5. **`airbnb/notebook.ipynb`** – Real‑world case study that combines everything.
6. Explore the notebooks under `data_cleaning/` for further practice.

---

## 📦 Requirements

A minimal `requirements.txt` is provided.  It contains the core libraries used in the notebooks:

```
$(cat requirements.txt)
```

If you want a more reproducible environment, you can generate an `environment.yml` (Conda) from the same list.

---

## 🤝 Contributing

We welcome improvements:
- Add new notebooks covering advanced topics (time‑series, merging, performance). 
- Improve explanations, add markdown cells, or correct typos.
- Update the dataset files or add new public datasets.

See `CONTRIBUTING.md` for the full guidelines.

---

## 📄 License

This repository is released under the **MIT License** – feel free to reuse and adapt the material.

---

Happy data wrangling! 🎉

