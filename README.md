# Consumer360 – Retail Customer Analytics (Project 1)

## Overview
Consumer360 is a retail analytics project focused on building a 360-degree customer view
and applying advanced analytical techniques such as RFM segmentation and Market Basket
Analysis to identify high-value customers, churn risks, and product affinity insights.

This repository is structured to follow a production-grade analytics workflow:
Raw Data → Cleaned Fact Tables → Analytical Models → Validated Outputs → Visualization.

---

## Project Objectives
- Build a clean and scalable Customer 360 data model
- Segment customers using RFM (Recency, Frequency, Monetary) analysis
- Statistically validate customer segments
- Discover product bundles using Association Rule Mining
- Prepare clean, reusable datasets for dashboarding (Power BI)

---

## Repository Structure
├── data
│   ├── raw
│   │   └── Sales_Transaction_v4a.csv
│   ├── interim
│   │   └── customer_360_base.csv
│   └── processed
│       ├── rfm_scored_customers.csv
│       ├── rfm_segment_validation.csv
│       └── market_basket_rules.csv
│
├── sql
│   ├── 01_raw_transactions_schema.sql
│   ├── 02_raw_transactions_ingestion.sql
│   ├── 03_fact_sales_cleaning.sql
│   ├── 04_dimension_tables.sql
│   └── 05_customer_360_single_customer_view.sql
│
├── python
│   ├── requirements.txt
│   ├── rfm
│   │   ├── rfm_scoring.py
│   │   ├── rfm_segmentation.py
│   │   └── rfm_validation.py
│   ├── basket
│   │   └── association_rules.py
│   └── run_week2_pipeline.py
│
├── docs
│   ├── assumptions.md
│   ├── data_dictionary.md
│   ├── rfm_logic.md
│   ├── rfm_validation.md
│   └── basket_analysis_design.md
│
└── README.md

---

## Data Flow Explanation

1. **Raw Data**
   - Original transactional CSV stored in `data/raw/`
   - No modifications applied

2. **Interim Data**
   - Output of SQL Customer 360 view
   - One row per customer
   - Acts as a bridge between SQL and Python analytics

3. **Processed Data**
   - Final analytical outputs used for dashboards
   - Includes RFM scores, segment validation, and basket rules

---

## Week-wise Execution Plan

### Week 1 – Data Engineering (SQL)
- Define ER diagram
- Create fact and dimension tables
- Clean raw transactions
- Build Single Customer View (Customer 360)

### Week 2 – Analytical Core (Python)
- RFM scoring and segmentation
- Statistical validation of segments
- Market Basket Analysis
- Export validated analytical datasets

---

## Key Validation Rules
- "Champions" segment must have the highest average revenue, frequency, and LTV
- Market Basket rules must have Lift > 1 (preferably > 1.5)
- All outputs must be reproducible and data-driven

---

## Tools & Libraries
- SQL (MySQL/PostgreSQL)
- Python (Pandas, NumPy, mlxtend, lifetimes)
- Power BI (Visualization – Week 3)

---

## Notes
- Week 2 logic is designed to be independent of Week 1 execution
- Real data tuning happens only after Customer 360 is finalized
- Clear separation between logic, validation, and outputs is enforced