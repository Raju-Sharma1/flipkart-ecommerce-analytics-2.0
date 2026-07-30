# Data Cleaning & Transformation

## Overview

Before performing exploratory data analysis (EDA), the dataset underwent a structured data cleaning and transformation process to improve its quality, consistency, and analytical reliability.

The cleaning process was carried out in two phases:

1. **Data Preprocessing** – Applied general business rules to handle missing values, standardize data formats, and validate data quality.
2. **Category Transformation** – Applied domain-specific business rules to correct incorrect product categories using brand and product information.

These steps produced a cleaner and more accurate dataset for subsequent analysis and business insight generation.

---

# Phase 1: Data Preprocessing

## Business Rules Applied

### 1. Missing Value Treatment

**Business Rule:**  
To ensure complete product information for analysis, missing values in the `size` column should be replaced using the most representative value available in the dataset.

**Action Taken**
- Missing values in the `size` column were imputed using the **mode (most frequently occurring value)**.

**Reason**
- The mode was selected as the imputation method based on the predefined business rule for this project, as it best represents the most common product size in the dataset.
- Maintains consistency across product records.
- Prevents missing values from affecting statistical analysis and visualizations.
- Preserves the existing distribution of the `size` column without introducing arbitrary values.

---

### 2. Shipping Weight Standardization

**Business Rule:**  
Shipping weights should be stored with a consistent level of numeric precision.

**Action Taken**
- Rounded all values in the `shipping_weight_g` column to two decimal places.

**Reason**
- Ensures consistency in numeric formatting.
- Removes unnecessary decimal precision.
- Improves readability and reporting.

---

### 3. Payment Mode Standardization

**Business Rule:**  
Multiple payment methods should follow a consistent delimiter format throughout the dataset.

**Action Taken**
- Replaced commas (`,`) with pipe symbols (`|`) in the `payment_modes` column.

**Reason**
- Standardizes the representation of multiple payment methods.
- Simplifies data parsing and text processing.
- Prevents potential conflicts when importing the dataset into a relational database, where commas may be interpreted as field separators or delimiters during data ingestion.
- Improves consistency across records for downstream data processing and analysis.

---

## Data Validation

Following preprocessing, the dataset was validated by:

- Reviewing dataset dimensions and data types.
- Identifying missing values.
- Checking for duplicate records.
- Reviewing descriptive statistics for numeric columns.
- Validating minimum and maximum values across numeric fields to identify potential anomalies.

These validation steps ensured the dataset met the required quality standards before further transformations were applied.

---

# Phase 2: Category Transformation

## Overview

During data validation, inconsistencies were identified within the **`category`** column. Several products were assigned to incorrect categories due to brand-level and product-level inconsistencies.

To improve classification accuracy, a set of business rules was applied to assign products to the appropriate category based on brand identity and product naming conventions.

---

## Business Rules Applied

### 1. Sports Brand Standardization

**Business Rule:**  
Products from dedicated sports brands should always belong to the **Sports** category.

**Brands Updated**

- Nike
- Adidas
- Reebok
- Puma

---

### 2. Electronics Brand Standardization

**Business Rule:**  
Products from dedicated electronics brands should always belong to the **Electronics** category.

**Brands Updated**

- Sony
- HP
- Dell
- Boat
- Whirlpool
- LG

---

### 3. Philips Product Classification

**Business Rule:**  
Since Philips manufactures products across multiple categories, product names were used to determine the appropriate category.

**Assigned to Electronics** when the product name contains:

- Ultra
- Series

**Assigned to Home & Kitchen** when the product name contains:

- Edition
- Prime
- Model

---

### 4. Apple Product Classification

**Business Rule:**  
Apple products were categorized based on identifiable naming patterns.

**Assigned to Mobiles** when the product name contains:

- Series
- Ultra

**Assigned to Electronics** when the product name contains:

- Edition
- Prime
- Model

---

### 5. Redmi Product Classification

**Business Rule:**  
Redmi products were categorized using product naming conventions.

**Assigned to Mobiles** when the product name contains:

- Series
- Ultra

**Assigned to Electronics** when the product name contains:

- Edition
- Prime
- Model

---

### 6. Samsung Product Classification

**Business Rule:**  
Samsung products span multiple categories and were classified using product name patterns.

**Assigned to Mobiles** when the product name contains:

- Series
- Ultra

**Assigned to Electronics** when the product name contains:

- Edition
- Prime
- Model

---

### 7. Brand-Level Category Standardization

The following brands were standardized to a single category based on their primary product offerings.

|Brand | Standardized Category |
|--------|-----------------------|
| Dell | Electronics |
| Sony | Electronics |
| HP | Electronics |
| Boat | Electronics |
| Whirlpool | Electronics |
| LG | Electronics |
| Prestige | Home & Kitchen |

---

# Final Outcome

The cleaning and transformation process significantly improved the overall quality of the dataset by:

- Handling missing values using predefined business rules.
- Standardizing numeric precision and text formatting.
- Validating data integrity before analysis.
- Correcting incorrectly assigned product categories.
- Enforcing brand-to-category consistency.
- Using product naming conventions to classify brands operating across multiple categories.
- Reducing inconsistencies that could impact business analysis and reporting.

The resulting dataset represents a cleaner, standardized, and more reliable version of the original data, making it suitable for exploratory data analysis (EDA), visualization, statistical analysis, and business insight generation.
