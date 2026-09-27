
#refreshing to recreate
#ALTER TABLE transactions DROP CONSTRAINT chk_customer_id;
#DROP TABLE customers; 
#DROP TABLE transactions;

#initialising customer & transaction tables
 
CREATE TABLE customers(
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

#ALTER TABLE customers AUTO_INCREMENT = 1000;

INSERT INTO customers(first_name, last_name) VALUES
	("John", "Wick"),
    ("John", "Ascott"),
	("Leo", "Chen");
    
CREATE TABLE transactions(
	transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    amount DECIMAL(5, 2),
    customer_id INT
    #CONSTRAINT chk_customer FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

ALTER TABLE transactions ADD CONSTRAINT chk_customer_id FOREIGN KEY(customer_id) REFERENCES customers(customer_id);

INSERT INTO transactions(customer_id, amount) VALUES
	(3, 9.99),
    (2, 31.50),
    (3, 1.59),
    (1, 10.99),
    (NULL, 20.99);
    
INSERT INTO customers(first_name, last_name) VALUES ("Puffy", "Pott");
    
    
#viewing objects - inner join

SELECT * FROM transactions INNER JOIN customers ON transactions.customer_id = customers.customer_id;
SELECT * FROM transactions LEFT JOIN customers ON transactions.customer_id = customers.customer_id;
SELECT * FROM transactions RIGHT JOIN customers ON transactions.customer_id = customers.customer_id;

SELECT transaction_id, amount, first_name, last_name
FROM transactions INNER JOIN customers ON transactions.customer_id = customers.customer_id;

#Functions SQL

#SELECT COUNT(amount) AS "Today's transactions" FROM transactions;
#SELECT MAX(amount) AS "Today's largest amount" FROM transactions;
#MIN(), AVG()
SELECT CONCAT(first_name, " ", last_name) AS "Full Name" FROM customers;

#Dropping objects
ALTER TABLE transactions DROP CONSTRAINT chk_customer_id;
DROP TABLE transactions;
DROP TABLE customers;


