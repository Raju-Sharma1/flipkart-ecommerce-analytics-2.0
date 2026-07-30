# ==========================================================
# Flipkart Product Listings
# Data Cleaning & Transformation
#
# This script prepares the raw dataset for analysis in
# two phases:
#
# Phase 1: Data Preprocessing
#   - Initial dataset assessment
#   - Missing value treatment
#   - Data standardization
#   - Data validation
#
# Phase 2: Category Transformation
#   - Brand-level category corrections
#   - Product-level category classification
#
# Output:
#   Accurate_Dataset.csv
# ==========================================================

import pandas as pd

# ==========================================================
# Load Raw Dataset
# ==========================================================

file_path = r"C:\Users\rajsh\OneDrive\Desktop\Personal Project\Analytics Project\Flipkart Product Listings\flipkart Product.csv"

df = pd.read_csv(file_path)

# ==========================================================
# PHASE 1 : DATA PREPROCESSING
# ==========================================================

# ----------------------------------------------------------
# Initial Dataset Assessment
# ----------------------------------------------------------

# Inspect dataset dimensions
df.shape

# Review data types and non-null values
df.info()

# Generate descriptive statistics
df.describe()

# ----------------------------------------------------------
# Missing Value Treatment
# ----------------------------------------------------------

# Inspect missing values
df.isnull().sum()

# Business Rule:
# Missing values in the 'size' column are replaced with
# the mode (most frequently occurring value).

df["size"] = df["size"].fillna(df["size"].mode()[0])

# ----------------------------------------------------------
# Duplicate Validation
# ----------------------------------------------------------

# Check for duplicate records.

df.duplicated().sum()

# ----------------------------------------------------------
# Data Standardization
# ----------------------------------------------------------

# Standardize numeric precision.

df["shipping_weight_g"] = df["shipping_weight_g"].round(2)

# Replace commas with pipe symbols to simplify
# future database imports and text parsing.

df["payment_modes"] = df["payment_modes"].str.replace(",", "|")

# ----------------------------------------------------------
# Numeric Data Validation
# ----------------------------------------------------------

# Review minimum and maximum values for all numeric
# columns to identify abnormal values.

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
# PHASE 2 : CATEGORY TRANSFORMATION
# ==========================================================

# ----------------------------------------------------------
# Brand-Level Category Standardization
# ----------------------------------------------------------

# Products from dedicated sports brands are assigned
# to the Sports category.

sports_brands = [
    "Nike",
    "Adidas",
    "Reebok",
    "Puma"
]

df.loc[df["brand"].isin(sports_brands), "category"] = "Sports"

# Products from dedicated electronics brands are assigned
# to the Electronics category.

electronics_brands = [
    "Sony",
    "HP",
    "Dell",
    "Boat",
    "Whirlpool",
    "LG"
]

df.loc[df["brand"].isin(electronics_brands), "category"] = "Electronics"

# Prestige products belong to Home & Kitchen.

df.loc[df["brand"] == "Prestige", "category"] = "Home & Kitchen"

# ----------------------------------------------------------
# Multi-Category Brand Classification
# ----------------------------------------------------------

# Some brands manufacture products across multiple
# product categories. Product names are used to
# determine the appropriate category.

# Philips:
# Products containing "Ultra" or "Series" are classified
# as Electronics, while products containing "Edition",
# "Prime", or "Model" are classified as Home & Kitchen.

# Mask 1: rows where brand is Philips
is_philips = flipkart['brand'] == 'Philips'

# Mask 2: product_name contains "Ultra" or "Series"
electronics_mask = flipkart['product_name'].str.contains('Ultra|Series', case=False, na=False)

# Mask 3: product_name contains "Edition", "Prime", or "Model"
home_kitchen_mask = flipkart['product_name'].str.contains('Edition|Prime|Model', case=False, na=False)

# Apply the updates
flipkart.loc[is_philips & electronics_mask, 'category'] = 'Electronics'
flipkart.loc[is_philips & home_kitchen_mask, 'category'] = 'Home & Kitchen'


# Apple:
# Apple products containing "Series" or "Ultra" are
# categorized as Mobiles. Products containing
# "Edition", "Prime", or "Model" are categorized
# as Electronics.

# Mask 1: rows where brand is Apple
is_apple = flipkart['brand'] == 'Apple'

# Mask 2: product_name contains "Series" or "Ultra"
mobiles_mask = flipkart['product_name'].str.contains('Series|Ultra', case=False, na=False)

# Mask 3: product_name contains "Edition", "Prime", or "Model"
electronics_mask = flipkart['product_name'].str.contains('Edition|Prime|Model', case=False, na=False)

# Apply the updates
flipkart.loc[is_apple & mobiles_mask, 'category'] = 'Mobiles'
flipkart.loc[is_apple & electronics_mask, 'category'] = 'Electronics'


# Redmi:
# Redmi products are categorized using the same
# product naming convention as Apple.

# Mask 1: rows where brand is Redmi
is_redmi = flipkart['brand'] == 'Redmi'

# Mask 2: product_name contains "Series" or "Ultra"
mobiles_mask = flipkart['product_name'].str.contains('Series|Ultra', case=False, na=False)

# Mask 3: product_name contains "Edition", "Prime", or "Model"
electronics_mask = flipkart['product_name'].str.contains('Edition|Prime|Model', case=False, na=False)

# Apply the updates
flipkart.loc[is_redmi & mobiles_mask, 'category'] = 'Mobiles'
flipkart.loc[is_redmi & electronics_mask, 'category'] = 'Electronics'


# Samsung:
# Samsung products are categorized based on
# product naming patterns.

# Mask 1: rows where brand is Samsung
is_samsung = flipkart['brand'] == 'Samsung'

# Mask 2: product_name contains "Series" or "Ultra"
mobiles_mask = flipkart['product_name'].str.contains('Series|Ultra', case=False, na=False)

# Mask 3: product_name contains "Edition", "Prime", or "Model"
electronics_mask = flipkart['product_name'].str.contains('Edition|Prime|Model', case=False, na=False)

# Apply the updates
flipkart.loc[is_samsung & mobiles_mask, 'category'] = 'Mobiles'
flipkart.loc[is_samsung & electronics_mask, 'category'] = 'Electronics'


# ----------------------------------------------------------
# Brand-Level Category Standardization
# ----------------------------------------------------------
# These brands primarily manufacture products belonging
# to a single category and are therefore standardized
# accordingly.

# Dell:
flipkart.loc[flipkart['brand'] == 'Dell', 'category'] = 'Electronics'

# Sony:
flipkart.loc[flipkart['brand'] == 'Sony', 'category'] = 'Electronics'

# HP:
flipkart.loc[flipkart['brand'] == 'HP', 'category'] = 'Electronics'

# Boat:
flipkart.loc[flipkart['brand'] == 'Boat', 'category'] = 'Electronics'

# Prestige:
flipkart.loc[flipkart['brand'] == 'Prestige', 'category'] = 'Home & Kitchen'

# Whirlpool:
flipkart.loc[flipkart['brand'] == 'Whirlpool', 'category'] = 'Electronics'

# LG:
flipkart.loc[flipkart['brand'] == 'LG', 'category'] = 'Electronics'

# ==========================================================
# Save Processed Dataset
# ==========================================================

output_path = r"C:\Users\rajsh\OneDrive\Desktop\Personal Project\Analytics Project\Flipkart Product Listings\Accurate_Dataset.csv"

df.to_csv(output_path, index=False)
