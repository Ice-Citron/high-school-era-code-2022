
#DROP TABLE transactions;

#Primary keys constraint uniquely identifies each record in a table (each column MUST be unique + not null)
#each table can only have 1 primary key - CREATE & ALTER
CREATE TABLE transactions(
	#transaction_id INT PRIMARY KEY,
    transaction_id INT,
	amount DECIMAL(5, 2) 
);

ALTER TABLE transactions ADD CONSTRAINT PRIMARY KEY(transaction_id);
#SELECT * FROM transactions;

DROP TABLE transactions;

#Auto increment
CREATE TABLE transactions(
	transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    amount DECIMAL(5, 2)
);

ALTER TABLE transactions AUTO_INCREMENT = 1000;

INSERT INTO transactions(amount) VALUES 
	(4.99), 
	(2.89), 
    (3.28);

#SELECT * FROM transactions;
DROP TABLE transactions;

#DROP TABLE customers;

#Foreign Keys - Customer table & Transaction table
CREATE TABLE customers(
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
	first_name VARCHAR(50), 
    last_name VARCHAR(50)
);

ALTER TABLE customers AUTO_INCREMENT = 1000;

INSERT INTO customers(first_name, last_name) VALUES 
	("Fred", "Fish"),
    ("Jaemus", "Li"),
    ("Ella", "Medarda");

SELECT * FROM customers;


CREATE TABLE transactions( #applying foreign key constraint
	transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    amount DECIMAL(5, 2)
    #, CONSTRAINT fk_customer_id FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

#ALTER TABLE transactions DROP FOREIGN KEY fk_customer_id;
ALTER TABLE transactions ADD CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customers(customer_id);

INSERT INTO transactions(customer_id, amount) VALUES 
	(1002, 4.89),
    (1001, 2.99),
    (1002, 3.98),
    (1000, 0.57);
    
SELECT * FROM transactions;


#need to remove foreign key constrain first before deleting table
ALTER TABLE transactions DROP CONSTRAINT fk_customer_id;
DROP TABLE customers;
DROP TABLE transactions;






