
#UPDATE & DELETE
UPDATE employees SET hourly_pay = 12.00, hire_date = "2023-03-01" WHERE employee_id = 7.50;
DELETE FROM employees WHERE hourly_pay = 12.00;

SET AUTOCOMMIT = OFF;
COMMIT;
ROLLBACK;


#Testing current date and time
CREATE TABLE timetest(
	my_date DATE,
	my_time TIME,
    my_datetime DATETIME
);
INSERT INTO timetest VALUES
	(CURRENT_DATE(), CURRENT_TIME, NOW()),
    (CURRENT_DATE() + 1, CURRENT_TIME - 60, NOW() - 3600);
UPDATE timetest SET my_date = CURRENT_DATE() - 1, my_datetime = my_datetime - 3600 WHERE my_time = CURRENT_TIME();

DROP TABLE timetest;


#Unique columns - initialisation & altering
CREATE TABLE uniquetest(
	product_id int,
    product_name VARCHAR(50) UNIQUE,
    price decimal(4, 2)
);

ALTER TABLE uniquetest ADD CONSTRAINT UNIQUE(product_id);









