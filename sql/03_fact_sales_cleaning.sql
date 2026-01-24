-- Clean raw transactions into fact table

USE consumer360;

DROP TABLE IF EXISTS fact_sales;

CREATE TABLE fact_sales AS
SELECT
    TransactionNo AS transaction_no,
    STR_TO_DATE(Date, '%m/%d/%Y') AS transaction_date,
    ProductNo AS product_no,
    ProductName AS product_name,
    CustomerNo AS customer_no,
    Country AS country,
    Quantity AS quantity,
    Price AS price,
    (Quantity * Price) AS total_amount
FROM raw_transactions
WHERE
    CustomerNo IS NOT NULL
    AND TRIM(CustomerNo) <> ''
    AND Quantity > 0;