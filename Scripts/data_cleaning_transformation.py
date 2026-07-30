# ==========================================================
# Flipkart Product Listings
# Data Cleaning & Transformation
#
# This script performs the complete preprocessing workflow:
# 1. Initial data assessment
# 2. Missing value treatment
# 3. Data standardization
# 4. Data validation
# 5. Category corrections using predefined business rules
# ==========================================================

import pandas as pd

# ==========================================================
# Load Dataset
# ==========================================================

file_path = r"C:\Users\rajsh\OneDrive\Desktop\Personal Project\Analytics Project\Flipkart Product Listings\flipkart Product.csv"

df = pd.read_csv(file_path)

# ==========================================================
# Initial Dataset Assessment
# ==========================================================

# Inspect dataset dimensions
df.shape

# Review data types and non-null values
df.info()

# Generate descriptive statistics
df.describe()

# ==========================================================
# Missing Value Treatment
# ==========================================================

# Inspect missing values
df.isnull().sum()

# Business Rule:
# Missing product sizes are replaced using the mode
# (most frequently occurring value).

df["size"] = df["size"].fillna(df["size"].mode()[0])

# ==========================================================
# Duplicate Validation
# ==========================================================

# Check for duplicate records.
# No duplicate rows were identified.

df.duplicated().sum()

# ==========================================================
# Data Standardization
# ==========================================================

# Standardize numeric precision

df["shipping_weight_g"] = df["shipping_weight_g"].round(2)

# Replace commas with pipe symbols to simplify future
# database imports and text parsing.

df["payment_modes"] = df["payment_modes"].str.replace(",", "|")

# ==========================================================
# Numeric Data Validation
# ==========================================================

# Review the minimum and maximum values for every
# numeric column to identify abnormal values.

numeric_columns = df.select_dtypes(include="number")

summary = []

for column in numeric_columns.columns:

    print("-" * 40)
    print(f"Column : {column}")
    print(f"Minimum: {numeric_columns[column].min()}")
    print(f"Maximum: {numeric_columns[column].max()}")

    summary.append({
        "column": column,
        "min": numeric_columns[column].min(),
        "max": numeric_columns[column].max()
    })

summary = pd.DataFrame(summary)

# ==========================================================
# Category Corrections
# ==========================================================

# Dedicated sports brands

sports_brands = [
    "Nike",
    "Adidas",
    "Reebok",
    "Puma"
]

df.loc[df["brand"].isin(sports_brands), "category"] = "Sports"

# Dedicated electronics brands

electronics_brands = [
    "Sony",
    "HP",
    "Dell",
    "Boat",
    "Whirlpool",
    "LG"
]

df.loc[df["brand"].isin(electronics_brands), "category"] = "Electronics"

# Prestige products belong to Home & Kitchen

df.loc[df["brand"] == "Prestige", "category"] = "Home & Kitchen"

# ==========================================================
# Multi-category Brand Classification
# ==========================================================

# These brands manufacture products belonging to
# multiple categories. Product names are therefore
# used to determine the appropriate category.

classification_rules = {

    "Philips": {
        "Electronics": "Ultra|Series",
        "Home & Kitchen": "Edition|Prime|Model"
    },

    "Apple": {
        "Mobiles": "Series|Ultra",
        "Electronics": "Edition|Prime|Model"
    },

    "Samsung": {
        "Mobiles": "Series|Ultra",
        "Electronics": "Edition|Prime|Model"
    },

    "Redmi": {
        "Mobiles": "Series|Ultra",
        "Electronics": "Edition|Prime|Model"
    }
}

for brand, rules in classification_rules.items():

    brand_mask = df["brand"] == brand

    for category, pattern in rules.items():

        pattern_mask = df["product_name"].str.contains(
            pattern,
            case=False,
            na=False
        )

        df.loc[
            brand_mask & pattern_mask,
            "category"
        ] = category

# ==========================================================
# Save Clean Dataset
# ==========================================================

output_path = r"C:\Users\rajsh\OneDrive\Desktop\Personal Project\Analytics Project\Flipkart Product Listings\Accurate_Dataset.csv"

df.to_csv(output_path, index=False)
