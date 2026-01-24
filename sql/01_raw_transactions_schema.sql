-- Create database and raw landing table

CREATE DATABASE IF NOT EXISTS consumer360;
USE consumer360;

DROP TABLE IF EXISTS raw_transactions;

CREATE TABLE raw_transactions (
    TransactionNo VARCHAR(20),
    Date VARCHAR(20),          -- stored as text intentionally
    ProductNo VARCHAR(20),
    ProductName VARCHAR(255),
    Price DECIMAL(10,2),
    Quantity INT,
    CustomerNo VARCHAR(20),
    Country VARCHAR(100)
);