-- =========================
-- Dimension Tables
-- =========================

-- 1. Geography Dimension
CREATE TABLE IF NOT EXISTS dim_geography AS
SELECT DISTINCT
    country AS country_name
FROM fact_sales
WHERE country IS NOT NULL;


-- 2. Customer Dimension
CREATE TABLE IF NOT EXISTS dim_customer AS
SELECT DISTINCT
    customer_no AS customer_id,
    country     AS country_name
FROM fact_sales
WHERE customer_no IS NOT NULL;


-- 3. Product Dimension
CREATE TABLE IF NOT EXISTS dim_product AS
SELECT DISTINCT
    product_no   AS product_id,
    product_name
FROM fact_sales
WHERE product_no IS NOT NULL
  AND product_name IS NOT NULL;


-- 4. Date Dimension
CREATE TABLE IF NOT EXISTS dim_date AS
SELECT DISTINCT
    transaction_date AS date_id,
    YEAR(transaction_date)  AS year,
    MONTH(transaction_date) AS month,
    DAY(transaction_date)   AS day
FROM fact_sales
WHERE transaction_date IS NOT NULL;


-- 5. Customer Segment Dimension (static business dimension)
CREATE TABLE IF NOT EXISTS dim_customer_segment (
    segment_name VARCHAR(50) PRIMARY KEY
);

INSERT IGNORE INTO dim_customer_segment (segment_name) VALUES
('Champions'),
('Loyal'),
('Potential Loyalist'),
('Needs Attention'),
('Price Sensitive'),
('About to Sleep'),
('Hibernating'),
('Lost');
