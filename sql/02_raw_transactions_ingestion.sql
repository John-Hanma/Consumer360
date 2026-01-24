-- Create Data Ingestion

USE consumer360;

LOAD DATA LOCAL INFILE '/absolute/path/to/Sales_Transaction_v4a.csv' -- Add your csv file for Data ingestion.
INTO TABLE raw_transactions
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    TransactionNo,
    Date,
    ProductNo,
    ProductName,
    Price,
    Quantity,
    CustomerNo,
    Country
);

