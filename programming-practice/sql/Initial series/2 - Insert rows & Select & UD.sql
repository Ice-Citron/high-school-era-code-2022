#inserting values
INSERT INTO employees VALUES 
	(1, "John", "Ashworth", 11.0, "2019-01-23"),
    (2, "Josh", "Loi", 27.50, "2018-03-27"),
    (3, "Shang", "Luo", 15.3, "2022-01-30"),
    (4, "Jason", "Chen", 20.3, "2018-12-31");

#alternative means of inserting values
INSERT INTO employees(first_name, last_name, hiring_date) VALUES
	("Chen Ding", "Chan", "2023-08-23");

SELECT * FROM employees;
SELECT first_name, last_name FROM employees WHERE employee_id = 2;
SELECT last_name, first_name FROM employees WHERE hourly_pay IS NOT NULL;


#ALTER TABLE employees ADD CONSTRAINT chk_hourly_pay CHECK (hourly_pay >= 10.0); 
#ALTER TABLE employees DROP CHECK chk_hourly_pay;
#SELECT * FROM employees;