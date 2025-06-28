-- This script creates the database 'hbtn_0d_usa' and the table 'cities' inside it
-- The 'cities' table has:
-- id INT, PRIMARY KEY, UNIQUE, NOT NULL, AUTO_INCREMENT
-- state_id INT, NOT NULL, FOREIGN KEY referencing 'states(id)'
-- name VARCHAR(256) NOT NULL
-- The script will not fail if the database or table already exist

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_state FOREIGN KEY (state_id) REFERENCES states(id)
);
