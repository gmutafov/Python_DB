CREATE TABLE employees(
	id serial PRIMARY KEY NOT NULL,
	first_name VARCHAR(30),
	last_name VARCHAR(50),
	hiring_date date DEFAULT '2023-01-01',
	salary NUMERIC(10,2),
	devices_number INTEGER
);

CREATE TABLE departments(
	id serial PRIMARY KEY NOT NULL,
	name VARCHAR(50),
	code CHARACTER(3),
	description TEXT
);

CREATE TABLE issues(
	id serial PRIMARY KEY UNIQUE,
	description VARCHAR(150),
	date DATE,
	start TIMESTAMP
)