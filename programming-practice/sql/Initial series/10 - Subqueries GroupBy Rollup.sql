
DROP TABLE employees;
ALTER TABLE transactions DROP CONSTRAINT fk_customer_id;
DROP TABLE customers;
DROP TABLE transactions;

#Initialising list
CREATE TABLE employees(
	employee_id INT PRIMARY KEY AUTO_INCREMENT,
	first_name VARCHAR(30),
    last_name VARCHAR(30),
    hourly_pay DECIMAL(5, 2),
    job VARCHAR(40),
    hire_date DATE
);

ALTER TABLE employees ADD COLUMN supervisor_id INT AFTER hire_date;
ALTER TABLE employees MODIFY hire_date DATE DEFAULT(current_date());

INSERT INTO employees (first_name, last_name, hourly_pay, job, hire_date, supervisor_id) VALUES
	("John", "Ashworth", 51.0, "Manager", "2019-01-23", NULL),
    ("Josh", "Loi", 27.50, "Assistant Manager", "2018-03-27", 1),
    ("Shang", "Luo", 15.3, "Cook", "2022-01-30", 2),
    ("Jason", "Chen", 20.3, "Janitor", "2018-12-31", 2),
    ("Zarif", "Khairun", 12.05, "Cook", "2021-10-21", 2),
    ("Roy", "Youn", 19.75, "Cashier", "2022-09-30", 2);


#Subqueries
SELECT CONCAT(src.first_name, " ", src.last_name) AS "full_name", src.hourly_pay, (SELECT AVG(hourly_pay) FROM employees) AS "avg_pay", 
	   CONCAT(main.first_name, " ", main.last_name) AS "supervisor_name"
FROM employees AS src LEFT JOIN employees AS main ON src.supervisor_id = main.employee_id; 

SELECT first_name, last_name, hourly_pay FROM employees WHERE (SELECT AVG(hourly_pay) FROM employees) < hourly_pay;


#initialising transactions and customers table
CREATE TABLE customers(
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(40),
    last_name VARCHAR(40)
);

INSERT INTO customers(first_name, last_name) VALUES
	("Ben", "Chang"),
    ("Yumin", "Lee"),
    ("Joseph", "Stalin"),
    ("Jong Un", "Kim"),
    ("Donald", "Trump"),
    ("Joe", "Biden");

CREATE TABLE transactions(
	transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    amount DECIMAL(5, 2),
    customer_id INT,
    transfer_date DATE DEFAULT(current_date())
);

ALTER TABLE transactions ADD CONSTRAINT fk_customer_id FOREIGN KEY(customer_id) REFERENCES customers(customer_id);

INSERT INTO transactions(amount, customer_id, transfer_date) VALUES
	(33.20, 1, "2021-09-02"), (21.99, 2, "2022-09-02"), (5.99, 3, "2022-09-02"), (156.39, 4, "2022-09-02"), (1.59, 2, "2022-09-02"),
    (20.99, 5, "2022-09-02"), (31.99, NULL, "2021-09-02"), (33.20, 1, current_date()), (21.99, 2, current_date()), (5.99, 3, current_date()),
    (33.39, 4, current_date()), (65.59, 2, current_date()), (34.99, 5, current_date()), (56.99, NULL, "2021-09-02"), (33.20, 1, "2023-09-02"),
    (11.99, 2, "2022-09-02"), (22.99, 3, "2022-09-02"), (156.39, 4, "2022-09-02"), (1.59, 2, "2022-09-02"), (465.99, 5, "2022-09-02"),
	(22.99, NULL, "2021-09-02"), (33.20, 1, current_date()), (53.99, 2, current_date()), (2.99, 3, current_date()), (22.39, 4, current_date()),
    (1.59, 2, current_date()), (89.99, 5, current_date()), (12.99, NULL, "2021-09-02");
    
-- SELECT DISTINCT customer_id FROM transactions WHERE NOT (customer_id IS NULL);
-- SELECT customer_id FROM transactions WHERE customer_id IS NOT NULL;

SELECT CONCAT(first_name, " ", last_name) AS "full_name" FROM customers WHERE  
customers.customer_id IN (SELECT DISTINCT customer_id FROM transactions WHERE customer_id IS NOT NULL);



#GROUP BY CLAUSE
SELECT customer_id, SUM(amount) AS "transfer_date_SUM", SUM(amount) AS "customer_id_SUM", transfer_date 
FROM transactions GROUP BY customer_id, transfer_date ORDER BY customer_id ASC;
-- MAX(), MIN(), AVG(), COUNT()

SELECT * FROM transactions;
SELECT * FROM customers;
SELECT SUM(transactions.amount), transactions.customer_id, CONCAT(customers.first_name, " ", customers.last_name) AS "full_name" 
FROM transactions INNER JOIN customers ON transactions.customer_id = customers.customer_id GROUP BY customer_id;

#original template 
-- SELECT * FROM transactions;
-- SELECT * FROM customers;

SELECT SUM(transactions.amount) AS "sum_amount", transactions.customer_id, CONCAT(customers.first_name, " ", customers.last_name) AS "full_name", transactions.transfer_date
FROM transactions INNER JOIN customers ON transactions.customer_id = customers.customer_id GROUP BY transactions.customer_id, transactions.transfer_date;

SELECT SUM(transactions.amount) AS "sum_amount", transactions.customer_id, CONCAT(customers.first_name, " ", customers.last_name) AS "full_name"
FROM transactions INNER JOIN customers ON transactions.customer_id = customers.customer_id GROUP BY transactions.customer_id
HAVING SUM(transactions.amount) > 20;

###When using GROUP BY CLAUSE, need to use 'ON' instead of 'WHERE'

-- SELECT SUM(amount) AS "SUM_customer-id", customer_id FROM transactions GROUP BY customer_id;
-- SELECT SUM(amount) AS "SUM_transfer-date", transfer_date FROM transactions GROUP BY transfer_date;



#ROLL UP Clause
SELECT SUM(amount) AS "SUM_customer-id", customer_id FROM transactions GROUP BY customer_id WITH ROLLUP;
SELECT COUNT(transaction_id) AS "Number-of-transactions", transfer_date FROM transactions GROUP BY transfer_date WITH ROLLUP;

SELECT customer_id, COUNT(transaction_id) AS "# of orders", SUM(amount) AS "Money Transferred Sum" FROM transactions #WHERE customer_id IS NOT NULL
GROUP BY customer_id WITH ROLLUP;


-- ANY_VALUE attempt - Most Successful (Bypasses 'ONLY_FULL_GROUP_BY')
SELECT transactions.customer_id, COUNT(transactions.transaction_id) AS "# of orders", SUM(transactions.amount) AS "Money Transferred Sum", 
	   ANY_VALUE(CONCAT(customers.first_name, " ", customers.last_name)) AS "full_name" FROM transactions INNER JOIN customers 
ON transactions.customer_id = customers.customer_id GROUP BY transactions.customer_id WITH ROLLUP;

-- ANY_VALUE GPT modification attempt
SELECT 
    transactions.customer_id,
    COUNT(transactions.transaction_id) AS "# of orders",
    SUM(transactions.amount) AS "Money Transferred Sum",
    SUBSTRING_INDEX(GROUP_CONCAT(CONCAT(customers.first_name, ' ', customers.last_name) ORDER BY CONCAT(customers.first_name, ' ', customers.last_name) DESC), ',', 1) as full_name
FROM 
    transactions 
INNER JOIN 
    customers ON transactions.customer_id = customers.customer_id 
GROUP BY 
    transactions.customer_id
WITH ROLLUP;

-- CONCAT attempt
SELECT transactions.customer_id, COUNT(transactions.transaction_id) AS "# of orders", SUM(transactions.amount) AS "Money Transferred Sum", 
	   CONCAT(customers.first_name, " ", customers.last_name) AS "full_name" FROM transactions INNER JOIN customers
ON transactions.customer_id = customers.customer_id GROUP BY transactions.customer_id, CONCAT(customers.first_name, " ", customers.last_name) 
WITH ROLLUP;


###Error - also calculates the null valyes, rollup failure overall.
-- Original query without rollup
SELECT transactions.customer_id, COUNT(transactions.transaction_id) AS "# of orders", 
       SUM(transactions.amount) AS "Money Transferred Sum", 
       CONCAT(customers.first_name, " ", customers.last_name) AS "full_name" 
FROM transactions 
INNER JOIN customers ON transactions.customer_id = customers.customer_id 
GROUP BY transactions.customer_id, CONCAT(customers.first_name, " ", customers.last_name)

UNION ALL

-- Subtotals for each customer_id
SELECT transactions.customer_id, COUNT(transactions.transaction_id) AS "# of orders", 
       SUM(transactions.amount) AS "Money Transferred Sum", 
       NULL AS "full_name" 
FROM transactions 
INNER JOIN customers ON transactions.customer_id = customers.customer_id 
GROUP BY transactions.customer_id

UNION ALL

-- Grand total
SELECT NULL as customer_id, COUNT(transactions.transaction_id) AS "# of orders", 
       SUM(transactions.amount) AS "Money Transferred Sum", 
       NULL AS "full_name" 
FROM transactions;





