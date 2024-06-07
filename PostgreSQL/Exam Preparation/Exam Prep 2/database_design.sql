CREATE TABLE addresses(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE categories(
    id SERIAL PRIMARY KEY,
    name VARCHAR(10) NOT NULL
);

CREATE TABLE clients(
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE drivers(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    age INT NOT NULL ,
    rating NUMERIC(2) DEFAULT 5.5,
    CONSTRAINT ck_drivers_age_is_positive
        CHECK (age > 0)
);

CREATE TABLE cars(
    id SERIAL PRIMARY KEY,
    make VARCHAR(20) NOT NULL,
    model VARCHAR(20),
    year INT NOT NULL DEFAULT 0,
    mileage INT DEFAULT 0,
    condition CHAR(1) NOT NULL,
    category_id INT NOT NULL REFERENCES categories ON DELETE CASCADE ON UPDATE CASCADE
    CONSTRAINT ck_year_is_positive
        CHECK (year > 0)
    CONSTRAINT ck_car_mileage_is_positive
        CHECK (mileage > 0)
);

CREATE TABLE courses(
    id SERIAL PRIMARY KEY,
    from_address_id INT NOT NULL REFERENCES addresses,
    start TIMESTAMP NOT NULL,
    bill NUMERIC(10, 2) DEFAULT 10,
    car_id INT NOT NULL REFERENCES cars ON DELETE CASCADE ON UPDATE CASCADE,
    client_id INT NOT NULL REFERENCES clients ON DELETE CASCADE ON UPDATE CASCADE
    CONSTRAINT ck_bill_is_positive
        CHECK (bill > 0)
);

CREATE TABLE cars_drivers(
    car_id    INT NOT NULL REFERENCES cars ON UPDATE CASCADE ON DELETE CASCADE,
    driver_id INT NOT NULL REFERENCES drivers ON UPDATE CASCADE ON DELETE CASCADE
);