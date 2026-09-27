#NOT NULL COLUMN - initialising & altering
CREATE TABLE productlist(
	product_id INT,
    product_name VARCHAR(50),
    price DECIMAL(4, 2) NOT NULL
);

#altering changes both the data type and adds the NOT NULL CONSTRAINT
ALTER TABLE productlist MODIFY price DECIMAL(4, 2) NOT NULL;

SELECT * FROM productlist;
DROP TABLE productlist;


#CHECK constraint - initialising & altering
CREATE TABLE workerlist(
	employee_id INT,
    first_name VARCHAR(25),
    last_name VARCHAR(25),
    hourly_pay DECIMAL(5, 2),
    hire_date DATE,
    CONSTRAINT chk_hourly_pay CHECK (hourly_pay >= 10.0)
);	

ALTER TABLE workerlist ADD CONSTRAINT chk_hire_date CHECK(hire_date > "2000-01-01");
ALTER TABLE workerlist DROP CHECK chk_hire_date;

DROP TABLE workerlist;


#DEFAULT constraint 
CREATE TABLE productlist(
	product_id INT,
    product_name VARCHAR(50) UNIQUE,
    #price DECIMAL(4, 2) DEFAULT 0
    price DECIMAL(4, 2) 
);

INSERT INTO productlist VALUES
	(104, "hamburger", 21.00),
    (105, "straws", NULL),
    (106, "ketchup", NULL),
    (107, "coca-cola", 3.50);
DELETE FROM productlist WHERE product_id > 108;

#ALTER TABLE productlist MODIFY price DECIMAL(4, 2) DEFAULT 0;
ALTER TABLE productlist ALTER price SET DEFAULT 0;

#SELECT * FROM productlist WHERE price IS NULL;
DROP TABLE productlist;


