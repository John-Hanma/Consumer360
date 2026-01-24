-- Create customer-level RFM base view

USE consumer360;

DROP VIEW IF EXISTS single_customer_view;

CREATE VIEW single_customer_view AS
SELECT
    customer_no,

    -- Recency: days since last transaction
    DATEDIFF(
        (SELECT MAX(transaction_date) FROM fact_sales),
        MAX(transaction_date)
    ) AS recency_days,

    -- Frequency: number of transactions
    COUNT(DISTINCT transaction_no) AS frequency,

    -- Monetary: total spend
    SUM(total_amount) AS monetary

FROM fact_sales
GROUP BY customer_no;
