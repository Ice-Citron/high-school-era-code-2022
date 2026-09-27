
DROP TABLE employees;
ALTER TABLE transactions DROP CONSTRAINT fk_customer_id;
DROP TABLE customers;
DROP TABLE transactions;
DROP TABLE incomes;
DROP TABLE expenses;

#initialising employees 
CREATE TABLE employees(
	employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30),
    last_name VARCHAR(30), 
    hourly_pay DECIMAL(5, 2),
    job VARCHAR(40), 
    hire_date DATE
);

ALTER TABLE employees ADD CONSTRAINT chk_hourly_pay CHECK (employees.hourly_pay >= 10.0);
#ALTER TABLE employees ADD COLUMN job VARCHAR(40) AFTER hourly_pay;

INSERT INTO employees (first_name, last_name, hourly_pay, job, hire_date) VALUES 
	("Eugene", "Teo", 21.00, "Manager", "2021-01-23"),
    ("Jason", "Chen", 15.50, "Cook", "2020-03-22"),
    ("Samson", "Hong", 10.00, "Janitor", "2022-10-10"),
    ("Heng Jun", "Tian", 12.00, "Cook", "2021-03-11"),
    ("Jia Yao", "Ong", 17.50, "Cashier", "2021-09-11"),
    ("Jia Ying", "Lui", 12.00, "Assistant Manager", "2019-03-28");
    
#ordering by 2 columns result in even more internal comparison
SELECT * FROM employees ORDER BY first_name ASC, last_name DESC; 


#initialising customer & transaction
CREATE TABLE customers(
	customer_id INT PRIMARY KEY AUTO_INCREMENT, 
    first_name VARCHAR(30), 
    last_name VARCHAR(30)
);

ALTER TABLE customers AUTO_INCREMENT = 1000;

INSERT INTO customers(first_name, last_name) VALUES
	("Ben", "Chang"),
    ("Yumin", "Lee"),
    ("Ziyi", "Tan"),
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

INSERT INTO transactions(amount, customer_id) VALUES
	(33.20, 1000),
    (21.99, 1001),
    (5.99, 1002),
    (156.39, 1003),
    (1.59, 1001),
    (20.99, 1004), 
    (31.99, 1002);
    
SELECT transaction_id, first_name, last_name, amount, transactions.customer_id, transfer_date FROM 
	transactions INNER JOIN customers ON transactions.customer_id = customers.customer_id;

#LIMIT clause
SELECT * FROM customers ORDER BY first_name DESC LIMIT 4;
SELECT * FROM customers ORDER BY first_name DESC LIMIT 3, 2; #thus returns 2 values, after an offset of 3 values


#initialising for union function
CREATE TABLE incomes(
	income_id INT PRIMARY KEY AUTO_INCREMENT, 
	income_name VARCHAR(50),
    income DECIMAL(9,2)
);

CREATE TABLE expenses(
	expense_id INT PRIMARY KEY AUTO_INCREMENT,
    expense_name VARCHAR(50),
    expense DECIMAL(9, 2)
);

INSERT INTO incomes(income_name, income) VALUES
	("Share dividends", 99000),
    ("Tax payback", 10000),
    ("Invoice returns", 2000),
    ("Merger", 100000);
    
INSERT INTO expenses(expense_name, expense) VALUES
	("Wages", -20000),
    ("Tax", -120000),
    ("Energy prices", -99999);

#UNION function -  only works if same column keys
(SELECT * FROM incomes) UNION (SELECT * FROM expenses);

#SELECT * FROM customers UNION SELECT hourly_pay, CONCAT(first_name, " ", last_name) AS "full_name", job FROM employees;
SELECT * FROM customers UNION  ALL SELECT hourly_pay, CONCAT(first_name, " ", last_name) AS "full_name", job FROM employees;
### 'UNION ALL' function outputs all values, regardless duplications



    
    
