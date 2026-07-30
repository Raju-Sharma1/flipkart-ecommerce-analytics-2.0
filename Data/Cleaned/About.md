# Data Cleaning & Transformation

## Overview

Before performing exploratory data analysis (EDA), the dataset underwent a series of data cleaning and transformation steps to improve the accuracy and consistency of the **`category`** column.

Several products were assigned to incorrect categories due to brand and product naming inconsistencies. These issues were identified and corrected using brand-specific and product-specific rules to ensure that each product belongs to its appropriate category.

---

## Transformations Performed

### 1. Corrected Sports Brand Categories

Products belonging to the following brands were reassigned to the **Sports** category:

- Nike
- Adidas
- Reebok
- Puma

---

### 2. Corrected Electronics Brand Categories

Products belonging to the following brands were reassigned to the **Electronics** category:

- Sony
- HP
- Dell
- Boat
- Whirlpool
- LG

---

### 3. Philips Product Classification

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

Apple products were categorized based on keywords in the product name.

**Assigned to Mobiles** when the product name contains:

- Series
- Ultra

**Assigned to Electronics** when the product name contains:

- Edition
- Prime
- Model

---

### 5. Redmi Product Classification

Redmi products were categorized using product name patterns.

**Assigned to Mobiles** when the product name contains:

- Series
- Ultra

**Assigned to Electronics** when the product name contains:

- Edition
- Prime
- Model

---

### 6. Samsung Product Classification

Samsung products were categorized using the same rule-based approach.

**Assigned to Mobiles** when the product name contains:

- Series
- Ultra

**Assigned to Electronics** when the product name contains:

- Edition
- Prime
- Model

---

### 7. Brand-Level Category Standardization

The following brands were standardized to a single category:

| Brand | Category |
|--------|----------|
| Dell | Electronics |
| Sony | Electronics |
| HP | Electronics |
| Boat | Electronics |
| Whirlpool | Electronics |
| LG | Electronics |
| Prestige | Home & Kitchen |

---

## Outcome

These transformations improve the overall quality of the dataset by:

- Correcting incorrectly assigned product categories.
- Ensuring brand-category consistency.
- Using product name patterns to classify brands that operate across multiple product categories.
- Reducing category-level inconsistencies before analysis.
- Providing a more reliable dataset for exploratory data analysis, visualization, and business insights.

The resulting dataset represents a cleaner and more accurate version of the original data, making subsequent analysis more meaningful and trustworthy.
