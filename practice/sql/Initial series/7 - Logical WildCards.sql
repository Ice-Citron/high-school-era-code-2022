
#initialising employee tables
DROP TABLE employees;

CREATE TABLE employees(
	employee_id INT PRIMARY KEY AUTO_INCREMENT, 
	first_name VARCHAR(25),
    last_name VARCHAR(25),
    hourly_pay DECIMAL(5, 2),
    hire_date DATE
);

ALTER TABLE employees ADD CONSTRAINT chk_hourly_pay CHECK(hourly_pay >= 10.0);

INSERT INTO employees (first_name, last_name, hourly_pay, hire_date) VALUES 
	("Eugene", "Teo", 21.00, "2021-01-23"),
    ("Jason", "Chen", 15.50, "2020-03-22"),
    ("Samson", "Hong", 10.00, "2022-10-10"),
    ("Heng Jun", "Tian", 12.00, "2021-03-11"),
    ("Jia Yao", "Ong", 17.50, "2021-09-11"),
    ("Jia Ying", "Lui", 12.00, "2019-03-28");

#adding a new column to employees table
ALTER TABLE employees ADD COLUMN job VARCHAR(30) AFTER hourly_pay;

UPDATE employees SET job = "Manager" WHERE employee_id = 1; 
UPDATE employees SET job = "Cashier" WHERE employee_id = 2;
UPDATE employees SET job = "Assistant Manager" WHERE employee_id = 3;
UPDATE employees SET job = "Janitor" WHERE employee_id = 4;
#UPDATE employees SET job = "Cook" WHERE employee_id = 5 OR employee_id = 6;
UPDATE employees SET job = "Cook" WHERE employee_id IN (5, 6);
    
SELECT * FROM employees;

#Wild Cards
#SELECT * FROM employees WHERE first_name LIKE "j%";		#finds wild card, first name that starts with letter 'j'
#SELECT * FROM employees WHERE last_name LIKE "%g";			#finds wild card, last name that ends with letter 'g'
SELECT * FROM employees WHERE job LIKE "_ook";				#finds wild card' '_', which means any job that starts with a random character
SELECT * FROM employees WHERE hire_date LIKE "____-03-__";





