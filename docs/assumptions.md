# Assumptions

This document outlines the key assumptions made during the design and implementation of the Consumer360 project.  
These assumptions ensure consistency, clarity, and reproducibility across data ingestion, modeling, analytics, and visualization.

---

## 1. Data Source Assumptions

- The retail transaction CSV represents a **single business entity** operating across multiple countries.
- The CSV file is assumed to be **historical and static** for the purpose of analysis.
- No incremental or real-time data ingestion is considered.
- All transactions in the dataset are assumed to be **valid business events**, except where explicitly filtered during cleaning.

---

## 2. Customer Assumptions

- `customer_no` uniquely identifies a customer across all transactions.
- Customers with missing or invalid `customer_no` values are excluded from analytical processing.
- Each customer belongs to **one country only**.
- Customer behavior is analyzed solely based on transaction history available in the dataset.

---

## 3. Transaction Assumptions

- Each `transaction_no` uniquely identifies a transaction.
- Each transaction is associated with **one customer** and **one product**.
- Transactions with negative or zero quantities are treated as returns or invalid and excluded during fact table creation.
- `total_amount` is derived as `price × quantity` after cleaning.

---

## 4. Product Assumptions

- `product_no` uniquely identifies a product.
- Product price is assumed to be **constant** across transactions.
- No product lifecycle changes (price updates, discontinuations) are modeled.

---

## 5. Date & Time Assumptions

- All transaction dates are assumed to be in the **same time zone**.
- Date values are converted and stored in a standard `DATE` format.
- Recency calculations use the **maximum transaction date in the dataset** as the reference date, not the current system date.

---

## 6. RFM Analysis Assumptions

- RFM metrics are calculated at the **customer level**.
- Definitions:
  - **Recency** = Days since last purchase
  - **Frequency** = Number of transactions
  - **Monetary** = Total spend
- Quantile-based binning is used for RFM scoring.
- Due to skewed distributions, duplicate quantile bins are automatically merged when required.
- R, F, and M scores are normalized to a **1–5 scale**, where higher values indicate better customer behavior.
- Each customer is assigned **exactly one RFM segment** using priority-based rules.

---

## 7. Data Modeling Assumptions

- The ER model is fully normalized to avoid redundancy.
- The star schema is intentionally denormalized to support analytical queries.
- Fact and dimension tables follow a **single-grain design**:
  - Fact table grain: one row per transaction
  - Customer view grain: one row per customer
- Surrogate keys are not used; natural keys are retained for simplicity.

---

## 8. Project Scope Assumptions

- Week 1 scope ends at creation of the `single_customer_view`.
- Python-based RFM scoring and segmentation are considered **Week 2 analytical tasks**.
- The project is designed as a **learning and demonstration pipeline**, not a live enterprise system.

---

## 9. Limitations

- No external enrichment data is used.
- No predictive or machine learning models are included.
- Customer churn and lifetime value are inferred only through RFM logic.
- Results are dependent on the completeness and quality of the provided dataset.

---

**End of Assumptions**