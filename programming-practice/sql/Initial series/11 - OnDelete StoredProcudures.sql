
ALTER TABLE transactions DROP CONSTRAINT fk_customer_id;
DROP TABLE customers;
DROP TABLE transactions;

#initialising customers and transactions table
CREATE TABLE customers(
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    referral_id INT DEFAULT(NULL),
    email VARCHAR(50)
);

INSERT INTO customers(first_name, last_name, email) VALUES
	("Ben", "Chang", "bchang@gmail.com"),
    ("Yumin", "Lee", "ylee@gmail.com"),
    ("Joseph", "Stalin", "jstalin@gmail.com"),
    ("Jong Un", "Kim", "jukim@gmail.com"),
    ("Donald", "Trump", "dtrump@gmail.com"),
    ("Joe", "Biden", "jbiden@gmail.com");

CREATE TABLE transactions(
	transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    amount DECIMAL(5, 2),
    customer_id INT,
    transfer_date DATE DEFAULT(current_date())
    #CONSTRAINT fk_customer_id FOREIGN KEY(customer_id) REFERENCES customers(customer_id) ON DELETE SET NULL / ON DELETE CASCADE
);

ALTER TABLE transactions ADD CONSTRAINT fk_customer_id FOREIGN KEY(customer_id) REFERENCES customers(customer_id);

INSERT INTO transactions(amount, customer_id, transfer_date) VALUES
	(33.20, 1, "2021-09-02"), (21.99, 2, "2022-09-02"), (5.99, 3, "2022-09-02"), (156.39, 4, "2022-09-02"), (1.59, 2, "2022-09-02"),
    (20.99, 5, "2022-09-02"), (31.99, NULL, "2021-09-02"), (33.20, 1, current_date()), (21.99, 2, current_date()), (5.99, 3, current_date()),
    (33.39, 4, current_date()), (65.59, 2, current_date()), (34.99, 5, current_date()), (56.99, NULL, "2021-09-02"), (33.20, 1, "2023-09-02"),
    (11.99, 2, "2022-09-02"), (22.99, 3, "2022-09-02"), (156.39, 4, "2022-09-02"), (1.59, 2, "2022-09-02"), (465.99, 5, "2022-09-02"),
	(22.99, NULL, "2021-09-02"), (33.20, 1, current_date()), (53.99, 2, current_date()), (2.99, 3, current_date()), (22.39, 4, current_date()),
    (1.59, 2, current_date()), (89.99, 5, current_date()), (12.99, NULL, "2021-09-02");


## Once the primary key has been deleted, the foreign key is no longer referencing to anything. There is 2 options:
-- ON DELETE SET NULL  = When a FK is deleted, replaces FK with NULL
-- ON DELETE CASCADE   = When a FK is deleted, delete row

ALTER TABLE transactions DROP CONSTRAINT fk_customer_id;
ALTER TABLE transactions ADD CONSTRAINT fk_customer_id FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
ON DELETE SET NULL;
-- ALTER TABLE transactions ADD CONSTRAINT fk_customer_id_null FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
-- ON DELETE CASCADE;


SELECT * FROM customers, transactions;
DELETE FROM customers WHERE customer_id = 4;

-- SET foreign_key_checks = 0;
-- SET foreign_key_checks = 1;

###The code doesn't work anymore, as foreign key checking has been reenabled
-- DELETE FROM customers WHERE customer_id = 3;
SELECT * FROM customers, transactions;



#STORED PROCURES (Procuderal functions)
DELIMITER $$
CREATE PROCEDURE get_customers()
BEGIN
	SELECT * FROM customers;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE find_customers(IN id INT)
BEGIN
	SELECT * FROM customers WHERE customer_id = id;
END$$
DELIMITER ;

CALL get_customers();
CALL find_customers(2);

DROP PROCEDURE get_customers;
DROP PROCEDURE find_customers;

