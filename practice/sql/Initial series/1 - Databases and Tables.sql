
#Create and Using a database
CREATE DATABASE test;
USE test;
#ALTER DATABASE test READ ONLY = 1;


CREATE TABLE employees (
	employee_id INT, 
    first_name VARCHAR(50),
    last_name VARCHAR(50), 
    hourly_pay DECIMAL(5,2),
    hiring_date DATE
);

#viewing and renaming
SELECT * FROM employees;
RENAME TABLE employees TO workers;

#adding "phone_number" column
ALTER TABLE workers ADD phone_number VARCHAR(15);

#changing "phone_number" column's key to "email"
ALTER TABLE workers RENAME COLUMN phone_number TO email;

#incrementing data size of phone_number to 100 characters
ALTER TABLE workers MODIFY COLUMN email VARCHAR(100);

#incrementing data size of phone number to 100 characters, but also changing the position of "email" column
ALTER TABLE workers MODIFY COLUMN email VARCHAR(100) AFTER last_name;
ALTER TABLE workers MODIFY COLUMN email VARCHAR(100) FIRST;

#dropping the "email" column
ALTER TABLE workers DROP COLUMN email;
SELECT * FROM workers;

DROP DATABASE test;
