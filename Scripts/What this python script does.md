# Flipkart Analytics 2.0 - Data Cleaning & Transformation

## Overview

This script performs the **data cleaning and transformation** phase of the **Flipkart Analytics 2.0** project.

The objective is to convert the raw Flipkart product dataset into a clean, standardized, and analysis-ready dataset that can be used for:

- Microsoft Excel Analysis
- SQL Analysis
- Power BI Dashboard Development

The cleaning process improves data quality by handling missing values, validating the dataset, standardizing formats, and correcting product categories using predefined business rules.

---

# Project Workflow

```
Raw Dataset
      │
      ▼
Data Cleaning & Transformation (Python)
      │
      ▼
Accurate_Dataset.csv
      │
      ├── Excel Analysis
      ├── SQL Analysis
      └── Power BI Dashboard
```

---

# Technologies Used

- Python
- Pandas

---

# Data Cleaning Process

The script is divided into two major phases.

## Phase 1 – Data Preprocessing

### Dataset Assessment

The script begins by examining the dataset to understand its overall structure.

Checks performed include:

- Dataset dimensions
- Column data types
- Non-null values
- Descriptive statistics

---

### Missing Value Treatment

Missing values are identified across all columns.

**Business Rule**

- Missing values in the **size** column are replaced with the column's mode (most frequent value).

---

### Duplicate Validation

The dataset is checked for duplicate records before analysis.

---

### Data Standardization

To improve consistency:

- `shipping_weight_g` is rounded to **2 decimal places**
- `payment_modes` values are converted from comma-separated values to pipe-separated values (`|`) to simplify SQL imports and text parsing.

Example:

```
Before:
UPI,Credit Card,COD

After:
UPI|Credit Card|COD
```

---

### Numeric Data Validation

All numeric columns are reviewed to identify abnormal values by inspecting:

- Minimum value
- Maximum value

This helps detect potential data quality issues before analysis.

---

# Phase 2 – Category Transformation

The raw dataset contains brands that manufacture products across multiple categories.

Instead of assigning every product from a brand to a single category, business rules were applied to improve classification accuracy.

---

## Brand-Level Category Standardization

Brands that manufacture products belonging to a single category are directly assigned to their appropriate category.

Examples include:

| Brand | Category |
|--------|----------|
| Nike | Sports |
| Adidas | Sports |
| Puma | Sports |
| Reebok | Sports |
| Sony | Electronics |
| Dell | Electronics |
| HP | Electronics |
| LG | Electronics |
| Boat | Electronics |
| Whirlpool | Electronics |
| Prestige | Home & Kitchen |

---

## Multi-Category Brand Classification

Some manufacturers produce products across multiple categories.

For these brands, the **product name** is used to determine the correct category.

Brands included:

- Samsung
- Apple
- Redmi
- Philips

Example business rules:

### Mobiles

Products containing keywords such as:

- Ultra
- Series

are categorized as:

```
Mobiles
```

---

### Electronics / Home & Kitchen

Products containing keywords such as:

- Prime
- Model
- Edition

are categorized according to the brand's product line.

This approach significantly improves category accuracy compared to assigning an entire brand to one category.

---

# Output

After all preprocessing and transformations are completed, the cleaned dataset is exported as:

```
Accurate_Dataset.csv
```

This dataset serves as the single source of truth for the remaining stages of the project.

---

# Next Steps

The cleaned dataset will be used for:

- Excel Descriptive Analysis
- SQL Server Analysis
- Power BI Dashboard Development

---

---

# Author

**Raju Sharma**

Building end-to-end analytics projects using **Python, Excel, SQL Server, and Power BI** to transform raw data into actionable business insights.
