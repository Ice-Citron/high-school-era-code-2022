
#DROP TABLE employees;
#DROP VIEW employee_attendance;

DROP TABLE customers;

CREATE TABLE customers(
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50), 
    last_name VARCHAR(50)
);

INSERT INTO customers(first_name, last_name) VALUES
	("Donald", "Trump"),
    ("Joe", "Biden"),
    ("Barack", "Obama"),
	("Jonatas", "Mancuso"),
    ("Julia", "Bella-inthof");
    
ALTER TABLE customers ADD COLUMN referral_id INT;

UPDATE customers SET referral_id = 1 WHERE customer_id IN (2, 3);
UPDATE customers SET referral_id = 3 WHERE customer_id IN (4, 5);

#SELECT * FROM customers;

#inner join, with alias 'AS'
#SELECT * FROM customers AS main INNER JO#initialising customer list
#IN customers AS src ON main.referral_id = src.customer_id;
SELECT main.customer_id, main.first_name, main.last_name, main.referral_id, CONCAT(src.first_name, " ", src.last_name) AS 'referred_by'
FROM customers AS main INNER JOIN customers AS src ON main.referral_id = src.customer_id;

SELECT main.customer_id, main.first_name, main.last_name, main.referral_id, CONCAT(src.first_name, " ", src.last_name) AS 'referred_by'
FROM customers AS main LEFT JOIN customers AS src ON main.referral_id = src.customer_id;

SELECT main.customer_id, main.first_name, main.last_name, main.referral_id, CONCAT(src.first_name, " ", src.last_name) AS 'referred_by'
FROM customers AS main RIGHT JOIN customers AS src ON main.referral_id = src.customer_id ORDER BY src.referral_id ASC, main.customer_id ASC;
#ordered from customer_id of src list, which is then ascended based on main.customer_id


#initialising employee list
CREATE TABLE employees(
	employee_id INT PRIMARY KEY AUTO_INCREMENT, 
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    hourly_pay DECIMAL(5, 2),
    job VARCHAR(40),
	hire_date DATE 
);

ALTER TABLE employees ADD COLUMN supervisor_id INT AFTER hire_date;
ALTER TABLE employees MODIFY supervisor_id VARCHAR(50);

INSERT INTO employees (first_name, last_name, hourly_pay, job, hire_date) VALUES
	("John", "Ashworth", 51.0, "Manager", "2019-01-23"),
    ("Josh", "Loi", 27.50, "Assistant Manager", "2018-03-27"),
    ("Shang", "Luo", 15.3, "Cook", "2022-01-30"),
    ("Jason", "Chen", 20.3, "Janitor", "2018-12-31"),
    ("Zarif", "Khairun", 12.05, "Cook", "2021-10-21"),
    ("Roy", "Youn", 19.75, "Cashier", "2022-09-30");

UPDATE employees SET supervisor_id = 2 WHERE employees.employee_id IN (3, 4, 5, 6);
UPDATE employees SET supervisor_id = 1 WHERE employees.employee_id = 2;

SELECT CONCAT(src.first_name, " ", src.last_name) AS "full_name", src.hourly_pay, src.job, src.hire_date, 
	   CONCAT(main.first_name, " ", main.last_name) AS "Supervisor_Name" FROM 
employees AS src LEFT JOIN employees AS main ON src.supervisor_id = main.employee_id;


#VIEWS - virtual tables | not real, can be interacted as if real table
CREATE VIEW employee_attendance AS SELECT first_name, last_name FROM employees;
SELECT * FROM employee_attendance ORDER BY first_name ASC;

ALTER TABLE customers ADD COLUMN email VARCHAR(50);
#CREATE VIEW customer_list AS SELECT email FROM customers; # - views acts as const reference

UPDATE customers SET email = "dtrump@gmail.com" WHERE customer_id = 1;
UPDATE customers SET email = "jbiden@gmail.com" WHERE customer_id = 2;
UPDATE customers SET email = "bobama@gmail.com" WHERE customer_id = 3;
UPDATE customers SET email = "jmancuso@gmail.com" WHERE customer_id = 4;
UPDATE customers SET email = "jbellainthof@gmail.com" WHERE customer_id = 5;

SELECT * FROM customers;


#Indexes
CREATE INDEX last_name_idx ON customers(last_name);
CREATE INDEX last_name_first_name_idx ON customers(last_name, first_name);
ALTER TABLE customers DROP INDEX last_name_idx;

SHOW INDEXES FROM customers;










