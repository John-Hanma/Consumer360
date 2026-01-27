# Data Dictionary

This document describes the structure, fields, and purpose of all tables used in the Consumer360 project.  
The data model follows a two-layer approach:
- Transactional layer (ER model)
- Analytical layer (Star Schema)

---

## 1. Transactional Tables (ER Model)

### 1.1 CUSTOMER

| Column Name | Data Type | Key | Description |
|------------|----------|-----|-------------|
| customer_no | STRING | PK | Unique identifier for each customer |
| country_code | STRING | FK | Country code representing customer location |

---

### 1.2 PRODUCT

| Column Name | Data Type | Key | Description |
|------------|----------|-----|-------------|
| product_no | STRING | PK | Unique identifier for each product |
| product_name | STRING | — | Name/description of the product |
| price | FLOAT | — | Unit price of the product |

---

### 1.3 TRANSACTION

| Column Name | Data Type | Key | Description |
|------------|----------|-----|-------------|
| transaction_no | STRING | PK | Unique transaction identifier |
| transaction_date | DATE | — | Date of transaction |
| quantity | INTEGER | — | Number of units purchased |
| total_amount | FLOAT | — | Total transaction value |
| customer_no | STRING | FK | References CUSTOMER.customer_no |
| product_no | STRING | FK | References PRODUCT.product_no |

---

### 1.4 COUNTRY

| Column Name | Data Type | Key | Description |
|------------|----------|-----|-------------|
| country_code | STRING | PK | ISO-style country identifier |
| country_name | STRING | — | Country name |
| region | STRING | — | Geographic region |

---

## 2. Analytical Tables (Star Schema)

### 2.1 FACT_SALES

| Column Name | Data Type | Key | Description |
|------------|----------|-----|-------------|
| transaction_no | STRING | PK | Unique transaction identifier |
| transaction_date | DATE | FK | References DIM_DATE.date |
| quantity | INTEGER | — | Units sold per transaction |
| total_amount | FLOAT | — | Revenue generated |
| customer_no | STRING | FK | References DIM_CUSTOMER.customer_no |
| product_no | STRING | FK | References DIM_PRODUCT.product_no |
| country_code | STRING | FK | References DIM_GEOGRAPHY.country_code |

---

### 2.2 DIM_CUSTOMER

| Column Name | Data Type | Key | Description |
|------------|----------|-----|-------------|
| customer_no | STRING | PK | Unique customer identifier |
| recency_days | INTEGER | — | Days since last purchase |
| frequency | INTEGER | — | Number of transactions |
| monetary | FLOAT | — | Total customer spend |
| r_score | INTEGER | — | Recency score (1–5) |
| f_score | INTEGER | — | Frequency score (1–5) |
| m_score | INTEGER | — | Monetary score (1–5) |
| rfm_code | STRING | — | Combined RFM code (e.g., 543) |
| segment_code | STRING | FK | References DIM_CUSTOMER_SEGMENT.segment_code |

---

### 2.3 DIM_PRODUCT

| Column Name | Data Type | Key | Description |
|------------|----------|-----|-------------|
| product_no | STRING | PK | Unique product identifier |
| product_name | STRING | — | Product name |
| price | FLOAT | — | Unit price |

---

### 2.4 DIM_DATE

| Column Name | Data Type | Key | Description |
|------------|----------|-----|-------------|
| date | DATE | PK | Calendar date |
| year | INTEGER | — | Year |
| quarter | INTEGER | — | Quarter of year |
| month | INTEGER | — | Month number |
| day | INTEGER | — | Day of month |
| weekday | STRING | — | Day name |

---

### 2.5 DIM_GEOGRAPHY

| Column Name | Data Type | Key | Description |
|------------|----------|-----|-------------|
| country_code | STRING | PK | Country identifier |
| country_name | STRING | — | Country name |
| region | STRING | — | Geographic region |

---

### 2.6 DIM_CUSTOMER_SEGMENT

| Column Name | Data Type | Key | Description |
|------------|----------|-----|-------------|
| segment_code | STRING | PK | Segment identifier |
| segment_name | STRING | — | Segment label (e.g., Champions, Loyal) |
| segment_description | STRING | — | Business definition of segment |

---

## 3. Notes

- Primary Keys (PK) uniquely identify records.
- Foreign Keys (FK) define relationships between tables.
- Fact tables store measurable events.
- Dimension tables store descriptive attributes used for filtering and grouping.
- RFM metrics are computed in SQL and Python and stored in the analytical layer.

---

**End of Data Dictionary**