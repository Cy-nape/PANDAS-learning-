#!/usr/bin/env python3
"""
Add beginner-friendly markdown explanation cells before every code cell
in each of the 9 target Jupyter notebooks.
"""

import json
import os
import copy

NOTEBOOKS_DIR = "/Users/sahilkulhar/Desktop/PANDAS/data_cleaning"

# ---------------------------------------------------------------------------
# Per-notebook metadata used to build the top-level title cell
# ---------------------------------------------------------------------------
NOTEBOOK_META = {
    "fashion.ipynb": {
        "title": "🧥 Fashion Dataset – Data Cleaning with Pandas",
        "dataset": "FashionDataset.csv",
        "concepts": [
            "Dropping unnamed/irrelevant columns",
            "Inspecting data types with `.info()` and `.dtypes`",
            "Cleaning column names",
            "Handling missing values in price and category columns",
        ],
        "learn": "You will learn how to load a fashion retail dataset, remove junk columns, understand data types, standardise column names, and deal with missing values – all essential first steps in any data-cleaning project.",
    },
    "hr.ipynb": {
        "title": "👔 HR Employee Attrition – Data Cleaning with Pandas",
        "dataset": "HR-Employee-Attrition.csv",
        "concepts": [
            "Exploring employee data",
            "Dropping irrelevant columns",
            "Detecting and removing duplicate rows",
            "Cleaning categorical columns",
            "Exporting the cleaned dataset to CSV",
        ],
        "learn": "You will learn how to explore an HR dataset, identify and remove columns that add no value, deal with duplicates, tidy up categorical data, and save the result for downstream analysis.",
    },
    "matplotlib.ipynb": {
        "title": "📊 Matplotlib Basics – Data Visualisation in Python",
        "dataset": "No external dataset – uses inline data",
        "concepts": [
            "Line plots",
            "Bar charts",
            "Scatter plots",
            "Histograms",
            "Customising colour, labels, and titles",
        ],
        "learn": "You will learn how to create the most common chart types with Matplotlib, control their appearance, and produce publication-ready plots from scratch.",
    },
    "netflix.ipynb": {
        "title": "🎬 Netflix Dataset – Data Cleaning with Pandas",
        "dataset": "netflix1.csv",
        "concepts": [
            "Loading and inspecting a CSV file",
            "Checking shape, columns, and data types",
            "Handling null values",
            "Dropping duplicate rows",
            "Cleaning date columns",
        ],
        "learn": "You will learn the standard first steps for cleaning a real-world streaming dataset – from loading it into a DataFrame all the way to exporting a clean version.",
    },
    "netflixlast.ipynb": {
        "title": "🎬 Netflix Titles – Deep Data Cleaning with Pandas",
        "dataset": "netflix_titles.csv",
        "concepts": [
            "Detecting missing values with `.isnull()`",
            "Filling missing values with `.fillna()`",
            "Dropping rows with `.dropna()`",
            "Detecting and removing duplicates",
            "Converting data types",
            "Exporting the cleaned dataset",
        ],
        "learn": "You will perform a thorough cleaning pass on the Netflix titles dataset, covering every major null-handling technique and finishing with a clean export ready for analysis.",
    },
    "notebook.ipynb": {
        "title": "🏠 Airbnb Open Data – Exploratory Data Analysis",
        "dataset": "Airbnb_Open_Data.csv",
        "concepts": [
            "Loading large CSV files",
            "Using `.head()` to preview data",
            "Using `.info()` to understand structure",
            "Listing column names",
        ],
        "learn": "You will learn the very first moves when encountering a large, real-world dataset – how to load it efficiently and quickly understand its shape, columns, and data types.",
    },
    "pyjanitor.ipynb": {
        "title": "🧹 PyJanitor – Automatic DataFrame Cleaning",
        "dataset": "Varies (demo DataFrames)",
        "concepts": [
            "`clean_names()` – standardise column names automatically",
            "`remove_empty()` – drop fully empty rows/columns",
            "`rename_column()` – rename columns fluently",
            "`filter_on()` – filter rows with a string expression",
            "`expand_column()` – expand list-like columns",
        ],
        "learn": "You will discover the PyJanitor library, which wraps common Pandas cleaning tasks into readable, chainable methods that make your cleaning pipelines shorter and easier to read.",
    },
    "sales.ipynb": {
        "title": "💰 Sales Data – Handling Missing Values with Pandas",
        "dataset": "sales.csv",
        "concepts": [
            "Dropping rows with missing values using `.dropna()`",
            "Filling missing values using `.fillna()`",
            "Strategies for handling NaN in sales figures",
            "Exporting the cleaned data to Excel",
        ],
        "learn": "You will work through a sales dataset to understand when to drop versus fill missing data, and how to deliver a clean Excel file to stakeholders.",
    },
    "zomatowala.ipynb": {
        "title": "🍽️ Zomato Restaurant Data – Full Cleaning Pipeline",
        "dataset": "Zomato restaurant dataset",
        "concepts": [
            "Null / missing-value checks",
            "Dropping unwanted columns",
            "Renaming columns",
            "Data-type conversion",
            "String cleaning (strip, replace, regex)",
            "Exporting the cleaned dataset",
        ],
        "learn": "This notebook walks you through a complete, end-to-end data-cleaning pipeline on restaurant data – 50+ steps that mirror what professional data analysts do every day.",
    },
}

# ---------------------------------------------------------------------------
# Helpers to generate explanatory markdown for a code cell
# ---------------------------------------------------------------------------

def _extract_text(source):
    """Return the source of a cell as a plain string."""
    if isinstance(source, list):
        return "".join(source)
    return source or ""


def _make_title_cell(nb_name):
    """Return a markdown cell dict for the notebook title/intro."""
    meta = NOTEBOOK_META.get(nb_name, {})
    title = meta.get("title", f"📓 {nb_name}")
    dataset = meta.get("dataset", "—")
    concepts = meta.get("concepts", [])
    learn = meta.get("learn", "")

    concepts_md = "\n".join(f"- {c}" for c in concepts)
    source = (
        f"# {title}\n\n"
        f"---\n\n"
        f"**📂 Dataset:** `{dataset}`\n\n"
        f"**🔑 Concepts covered:**\n{concepts_md}\n\n"
        f"**🎯 What you will learn:**  \n{learn}\n\n"
        f"---\n"
    )
    return {"cell_type": "markdown", "metadata": {}, "source": [source]}


def _explain_code(code_text, step_num, nb_name):
    """
    Generate a plain-English markdown explanation for a code cell.
    Uses keyword-matching to pick an appropriate explanation.
    Falls back to a generic description that quotes the first line.
    """
    code = code_text.strip()
    lines = [l for l in code.splitlines() if l.strip()]
    first = lines[0] if lines else ""

    # --- keyword rules (order matters – more specific first) ---
    rules = [
        # imports
        (["import pandas", "import pd"], "Import Pandas",
         "We start by importing the **Pandas** library and giving it the short alias `pd`. "
         "Pandas is the go-to Python library for working with tabular data (think: Excel, but in code).",
         "`import pandas as pd` — loads the library so we can use `pd.DataFrame`, `pd.read_csv()`, etc."),

        (["import numpy", "import np"], "Import NumPy",
         "We import **NumPy**, the numerical computing library. "
         "It is often used alongside Pandas for mathematical operations and to represent missing values (`np.nan`).",
         "`import numpy as np` — gives us fast array operations and constants like `np.nan`."),

        (["import matplotlib", "import plt", "from matplotlib"], "Import Matplotlib",
         "We import **Matplotlib** (and its `pyplot` module), the standard Python plotting library.",
         "`import matplotlib.pyplot as plt` — `plt` is the conventional alias for creating and displaying charts."),

        (["import janitor", "from janitor"], "Import PyJanitor",
         "We import **PyJanitor**, an add-on library that extends Pandas with cleaner, more readable data-cleaning methods.",
         "`import janitor` — once imported, PyJanitor methods become available directly on any DataFrame."),

        # loading data
        (["read_csv"], "Load the Dataset",
         "We read a CSV file from disk into a Pandas **DataFrame** – a table with rows and columns. "
         "This is almost always the very first step in a data-analysis project.",
         "`pd.read_csv()` — reads a comma-separated file and returns a DataFrame you can query and manipulate."),

        (["read_excel"], "Load an Excel File",
         "We load data from an Excel spreadsheet into a Pandas DataFrame.",
         "`pd.read_excel()` — reads one or more sheets from an `.xlsx` or `.xls` file."),

        # shape / info exploration
        (["df.shape", ".shape"], "Check the Dimensions",
         "We look at the **shape** of the DataFrame – how many rows and columns it has. "
         "This gives us a quick sense of how large the dataset is.",
         "`.shape` — returns a tuple `(rows, columns)`. No parentheses needed; it is a property, not a method."),

        (["df.head", ".head("], "Preview the First Rows",
         "We display the **first few rows** of the DataFrame to get a visual feel for the data.",
         "`.head(n)` — returns the first `n` rows (default 5). Great for a quick sanity-check after loading."),

        (["df.tail", ".tail("], "Preview the Last Rows",
         "We display the **last few rows** of the DataFrame.",
         "`.tail(n)` — returns the last `n` rows. Useful for checking if data was loaded completely."),

        (["df.info", ".info("], "Inspect Data Types and Non-Null Counts",
         "We call `.info()` to get a concise summary: column names, non-null counts, and data types. "
         "This is the fastest way to spot missing values and type mismatches.",
         "`.info()` — prints column names, number of non-null entries, and dtype for each column."),

        (["df.describe", ".describe("], "Statistical Summary",
         "We generate **descriptive statistics** (count, mean, min, max, percentiles) for all numeric columns. "
         "This helps identify outliers and understand the spread of values.",
         "`.describe()` — works on numeric columns by default; pass `include='all'` to include text columns too."),

        (["df.dtypes", ".dtypes"], "Check Data Types",
         "We inspect the **data type** of every column. "
         "Wrong types (e.g. a date stored as a string) are a very common data-quality issue.",
         "`.dtypes` — returns a Series mapping each column name to its dtype (`int64`, `object`, `float64`, etc.)."),

        (["df.columns", ".columns"], "List the Column Names",
         "We print all column names. This is handy for copy-pasting names and spotting typos or inconsistent naming.",
         "`.columns` — returns an Index object containing all column names."),

        # missing values
        (["isnull().sum", "isna().sum"], "Count Missing Values",
         "We count how many **null / NaN** values exist in each column. "
         "Missing data is one of the most common data-quality problems and must be addressed before analysis.",
         "`.isnull().sum()` — `.isnull()` creates a boolean mask (True where data is missing); `.sum()` counts the Trues per column."),

        (["isnull()", "isna()"], "Detect Missing Values",
         "We check for **missing (NaN/None)** values across the DataFrame.",
         "`.isnull()` — returns a boolean DataFrame: `True` where a value is missing, `False` where it is present."),

        (["notnull()", "notna()"], "Detect Non-Missing Values",
         "We check which cells have **actual (non-missing)** values.",
         "`.notnull()` — the inverse of `.isnull()`; returns `True` where data exists."),

        (["fillna"], "Fill Missing Values",
         "We **fill** missing values with a replacement – a constant, the column mean, or a forward/backward fill. "
         "This is called *imputation* and lets us keep rows that would otherwise be dropped.",
         "`.fillna(value)` — replaces every NaN in the column (or whole DataFrame) with `value`."),

        (["dropna"], "Drop Rows/Columns with Missing Values",
         "We **remove** rows (or columns) that contain missing values. "
         "Use this when the missing data is too sparse to impute reliably.",
         "`.dropna()` — by default drops any row with at least one NaN. Use `axis=1` to drop columns instead."),

        # duplicates
        (["duplicated()", "duplicated().sum"], "Detect Duplicate Rows",
         "We check whether any rows appear more than once in the dataset. "
         "Duplicates can skew aggregations and model training.",
         "`.duplicated()` — returns a boolean Series; `True` for every row that is an exact copy of a previous row."),

        (["drop_duplicates"], "Remove Duplicate Rows",
         "We **remove duplicate rows**, keeping only the first occurrence of each unique row.",
         "`.drop_duplicates()` — eliminates rows that are identical across all (or selected) columns."),

        # column management
        (["df.drop", ".drop("], "Drop Columns or Rows",
         "We **remove** one or more columns (or rows) from the DataFrame. "
         "Dropping irrelevant columns reduces noise and speeds up processing.",
         "`.drop(labels, axis=1)` — `axis=0` drops rows, `axis=1` drops columns. Add `inplace=True` to modify without reassigning."),

        (["rename("], "Rename Columns",
         "We **rename** columns to make them clearer or to match a naming convention.",
         "`.rename(columns={'old': 'new'})` — pass a dictionary mapping old names to new names."),

        (["str.lower", ".lower()"], "Convert Text to Lowercase",
         "We convert all text in a column to **lowercase**. "
         "This prevents 'Mumbai' and 'mumbai' from being treated as different values.",
         "`.str.lower()` — applies Python's `.lower()` string method to every element in a Series."),

        (["str.strip", ".strip()"], "Strip Whitespace",
         "We remove **leading and trailing whitespace** from string columns. "
         "Hidden spaces are a sneaky source of data-quality bugs.",
         "`.str.strip()` — removes spaces (and newlines) from both ends of each string."),

        (["str.replace", ".replace("], "Find and Replace Values",
         "We **replace** specific values or patterns in a column.",
         "`.str.replace(old, new)` — string-aware replacement; `.replace({old: new})` works on the whole Series for exact matches."),

        (["str.contains"], "Filter Rows by String Pattern",
         "We filter rows where a column's text **matches a pattern**.",
         "`.str.contains(pattern)` — returns a boolean mask; supports regular expressions by default."),

        # type conversion
        (["astype("], "Convert Data Types",
         "We **cast** a column to a different data type (e.g. string to integer, object to datetime). "
         "Correct types unlock the right operations – you can't do arithmetic on a string column.",
         "`.astype(dtype)` — returns a new Series with the values converted to `dtype`."),

        (["to_datetime", "pd.to_datetime"], "Parse Dates",
         "We convert a column of date strings into Pandas **datetime** objects. "
         "Once parsed as datetimes, we can sort, filter, and extract year/month/day easily.",
         "`pd.to_datetime(col)` — intelligently parses many date formats into `datetime64` dtype."),

        (["to_numeric", "pd.to_numeric"], "Convert to Numeric",
         "We coerce a column to a **numeric** type, forcing any unparseable strings to `NaN`.",
         "`pd.to_numeric(col, errors='coerce')` — converts valid numbers and turns invalid strings into `NaN` instead of raising an error."),

        # value counts / unique
        (["value_counts"], "Count Unique Values",
         "We count how many times each **unique value** appears in a column. "
         "This is perfect for exploring categorical data.",
         "`.value_counts()` — returns a Series sorted by frequency, highest first."),

        (["unique()", ".nunique()"], "Find Unique Values",
         "We retrieve the **distinct values** in a column to understand its categories.",
         "`.unique()` — returns an array of unique values; `.nunique()` returns just the count."),

        # sorting / resetting index
        (["sort_values"], "Sort the DataFrame",
         "We **sort** rows by one or more columns.",
         "`.sort_values(by='col')` — sorts ascending by default; pass `ascending=False` to reverse."),

        (["reset_index"], "Reset the Row Index",
         "We **reset** the integer index after filtering or dropping rows, so it runs 0, 1, 2… again.",
         "`.reset_index(drop=True)` — creates a fresh sequential index; `drop=True` discards the old index column."),

        # groupby / aggregation
        (["groupby"], "Group and Aggregate",
         "We **group** rows that share the same value in a column, then apply an aggregation (sum, mean, count…).",
         "`.groupby('col').agg(...)` — the split-apply-combine pattern: split data into groups, apply a function, combine results."),

        # export
        (["to_csv"], "Export to CSV",
         "We **save** the cleaned DataFrame to a CSV file on disk so it can be shared or used in another tool.",
         "`.to_csv('filename.csv', index=False)` — `index=False` prevents Pandas from writing the row-number column into the file."),

        (["to_excel"], "Export to Excel",
         "We **save** the cleaned DataFrame as an Excel file (`.xlsx`).",
         "`.to_excel('filename.xlsx', index=False)` — requires the `openpyxl` package; produces a file you can open directly in Excel."),

        # plotting
        (["plt.plot(", ".plot("], "Draw a Line Plot",
         "We create a **line plot** to visualise how values change across a sequence (e.g. over time).",
         "`plt.plot(x, y)` — connects data points with a line. Add `marker='o'` to also show individual points."),

        (["plt.bar(", ".bar("], "Draw a Bar Chart",
         "We create a **bar chart** to compare values across categories.",
         "`plt.bar(x, height)` — the height of each bar represents the value for that category."),

        (["plt.scatter(", ".scatter("], "Draw a Scatter Plot",
         "We create a **scatter plot** to visualise the relationship between two numeric variables.",
         "`plt.scatter(x, y)` — each data point becomes a dot; look for patterns, clusters, or outliers."),

        (["plt.hist(", ".hist("], "Draw a Histogram",
         "We create a **histogram** to see how a numeric variable is distributed across value ranges (bins).",
         "`plt.hist(data, bins=n)` — taller bars mean more values fall in that range."),

        (["plt.xlabel", "plt.ylabel", "plt.title", "plt.legend", "plt.show"], "Customise and Display the Chart",
         "We add **labels, a title, a legend**, and finally display the chart. "
         "These finishing touches make charts readable and presentation-ready.",
         "`plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.legend()`, `plt.show()` — formatting helpers that make your plot self-explanatory."),

        # pyjanitor
        (["clean_names"], "Standardise Column Names with PyJanitor",
         "We use PyJanitor's `clean_names()` to automatically convert all column names to **lowercase with underscores** (snake_case). "
         "Consistent naming makes code less error-prone.",
         "`df.clean_names()` — strips spaces, lowercases, and replaces special characters with underscores in one call."),

        (["remove_empty"], "Remove Empty Rows and Columns",
         "We use PyJanitor's `remove_empty()` to drop any **completely empty** rows or columns in one step.",
         "`df.remove_empty()` — removes rows/columns where every value is NaN or None."),

        (["rename_column"], "Rename a Column with PyJanitor",
         "We use PyJanitor's `rename_column()` for a clean, readable single-column rename.",
         "`df.rename_column('old_name', 'new_name')` — more readable than the standard `rename` for one-off renames."),

        (["filter_on"], "Filter Rows with PyJanitor",
         "We use PyJanitor's `filter_on()` to keep only rows that satisfy a **string condition**.",
         "`df.filter_on('column > value')` — accepts a plain-English-like condition string."),

        (["expand_column"], "Expand a List Column with PyJanitor",
         "We use PyJanitor's `expand_column()` to split a column containing **list-like values** into multiple binary indicator columns.",
         "`df.expand_column('col', sep=',')` — useful when one cell holds multiple categories separated by a delimiter."),

        # zomato-specific / general cleaning
        (["str.extract", "str.findall"], "Extract Values with Regex",
         "We use a **regular expression** to extract a specific pattern (e.g. a number) from a string column.",
         "`.str.extract(pattern)` / `.str.findall(pattern)` — applies a regex to each element and returns the captured groups."),

        (["apply("], "Apply a Custom Function",
         "We apply a **custom function** to every element (or row) in a Series/DataFrame.",
         "`.apply(func)` — the most flexible transformation; use a `lambda` for short one-liners or a named function for complex logic."),

        (["lambda"], "Use a Lambda (Anonymous) Function",
         "We use a **lambda** – a small, throwaway function defined in a single line – as part of a transformation.",
         "`lambda x: ...` — equivalent to `def f(x): return ...` but written inline, often inside `.apply()`."),

        (["map("], "Map Values to New Values",
         "We **replace each value** in a column using a dictionary or function lookup.",
         "`.map(dict_or_func)` — great for encoding categories (e.g. `{'Yes': 1, 'No': 0}`) or applying a lookup table."),
    ]

    for keywords, short_title, what_it_does, key_concept in rules:
        if any(kw.lower() in code.lower() for kw in keywords):
            source = (
                f"## Step {step_num}: {short_title}\n\n"
                f"**What this does:** {what_it_does}\n\n"
                f"**Key concept:** {key_concept}\n"
            )
            return {"cell_type": "markdown", "metadata": {}, "source": [source]}

    # --- generic fallback ---
    snippet = first[:80] + ("…" if len(first) > 80 else "")
    source = (
        f"## Step {step_num}: Code Block\n\n"
        f"**What this does:** The cell below runs the following Python code:\n\n"
        f"```python\n{snippet}\n```\n\n"
        f"Read the code carefully – each line either transforms the data or displays a result.\n"
    )
    return {"cell_type": "markdown", "metadata": {}, "source": [source]}


# ---------------------------------------------------------------------------
# Main processing logic
# ---------------------------------------------------------------------------

def process_notebook(nb_path):
    nb_name = os.path.basename(nb_path)
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    cells = nb.get("cells", [])
    new_cells = []

    # 1. Prepend the big title cell
    new_cells.append(_make_title_cell(nb_name))

    step = 1
    for cell in cells:
        if cell.get("cell_type") == "code":
            code_text = _extract_text(cell.get("source", ""))
            # Only add explanation if the cell has non-trivial content
            if code_text.strip():
                md_cell = _explain_code(code_text, step, nb_name)
                new_cells.append(md_cell)
                step += 1
            new_cells.append(cell)
        elif cell.get("cell_type") == "markdown":
            # Keep existing markdown cells as-is
            new_cells.append(cell)
        else:
            new_cells.append(cell)

    nb["cells"] = new_cells

    with open(nb_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    return nb_name, step - 1  # number of code cells processed


TARGET_NOTEBOOKS = [
    "fashion.ipynb",
    "hr.ipynb",
    "matplotlib.ipynb",
    "netflix.ipynb",
    "netflixlast.ipynb",
    "notebook.ipynb",
    "pyjanitor.ipynb",
    "sales.ipynb",
    "zomatowala.ipynb",
]

results = []
for nb_name in TARGET_NOTEBOOKS:
    nb_path = os.path.join(NOTEBOOKS_DIR, nb_name)
    if not os.path.exists(nb_path):
        results.append(f"  ❌ MISSING : {nb_name}")
        continue
    name, n_steps = process_notebook(nb_path)
    results.append(f"  ✅ {name}  ({n_steps} code cells annotated)")

print("\n🎉 All done!\n")
for r in results:
    print(r)
