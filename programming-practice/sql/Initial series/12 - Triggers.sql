
DROP TABLE expenses;
#DROP TRIGGER before_hourly_pay_update;
#DROP TRIGGER after_salary_delete;
#DROP TRIGGER after_salary_insert;
#DROP TRIGGER after_salary_update;
DROP TABLE employees;

#Initialising list
CREATE TABLE employees(
	employee_id INT PRIMARY KEY AUTO_INCREMENT,
	first_name VARCHAR(30),
    last_name VARCHAR(30),
    hourly_pay DECIMAL(5, 2), 
    job VARCHAR(40),
    hire_date DATE,
    CONSTRAINT CHECK(hourly_pay >= 10)
);

ALTER TABLE employees ADD COLUMN supervisor_id INT AFTER hire_date;
ALTER TABLE employees MODIFY hire_date DATE DEFAULT(current_date());
ALTER TABLE employees ADD COLUMN salary DECIMAL(10, 2) AFTER hourly_pay;

INSERT INTO employees (first_name, last_name, hourly_pay, job, hire_date, supervisor_id) VALUES
	("John", "Ashworth", 51.0, "Manager", "2019-01-23", NULL),
    ("Josh", "Loi", 27.50, "Assistant Manager", "2018-03-27", 1),
    ("Shang", "Luo", 15.3, "Cook", "2022-01-30", 2),
    ("Jason", "Chen", 20.3, "Janitor", "2018-12-31", 2),
    ("Zarif", "Khairun", 12.05, "Cook", "2021-10-21", 2),
    ("Roy", "Youn", 19.75, "Cashier", "2022-09-30", 2);
    
UPDATE employees SET salary = hourly_pay * 52 * 40;

CREATE TABLE expenses(
	expense_id INT PRIMARY KEY AUTO_INCREMENT,
    expense_name VARCHAR(50),
    expense_total DECIMAL(10, 2)
);

INSERT INTO expenses(expense_name, expense_total) VALUES
	("salary", 0),
    ("equipments", 0),
    ("supplies", 0),
    ("taxes", 0);


#TRIGGER - When an event happen, do something (e.g checks data, handles errors, auditing tables) [insert, update, delete]
CREATE TRIGGER before_hourly_pay_update BEFORE UPDATE ON employees 
FOR EACH ROW SET NEW.salary = NEW.hourly_pay * 52 * 40; -- Need 'NEW' keyword, to inform mySQL new values are being used instead

UPDATE employees SET hourly_pay = 15.50 WHERE employee_id = 5;
-- SHOW TRIGGERS;


##conventional method of inputting salary in Expenses Table
UPDATE expenses SET expense_total = (SELECT SUM(salary) FROM employees) WHERE expense_name = "salary";

##Trigger method of inputting or deleting salary in Expenses Table
CREATE TRIGGER after_salary_delete AFTER DELETE ON employees
FOR EACH ROW UPDATE expenses SET expenses_total = expense_total - OLD.salary WHERE expense_name = "salary"; -- For removing a employee from table

CREATE TRIGGER after_salary_insert AFTER INSERT on employees
FOR EACH ROW UPDATE expenses SET expenses_total = expense_total + NEW.salary WHERE expense_name = "salary"; -- For inserting a employee into the table

##Trigger method for updating hourly_pay in Employees table
CREATE TRIGGER after_salary_update AFTER UPDATE ON employees
FOR EACH ROW UPDATE expenses SET expense_total = expense_total + (NEW.salary - OLD.salary) WHERE expense_name = "salary;";

SELECT * FROM employees;
SELECT * FROM expenses;







 