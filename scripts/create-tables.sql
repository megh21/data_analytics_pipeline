-- create_tables.sql
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_type VARCHAR(255),
    date DATE,
    amount FLOAT
);
