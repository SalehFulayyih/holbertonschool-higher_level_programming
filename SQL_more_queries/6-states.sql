-- This script creates the database 'hbtn_0d_usa' and the table 'states' inside it
-- The 'states' table has:
-- id INT, PRIMARY KEY, UNIQUE, NOT NULL, AUTO_INCREMENT
-- name VARCHAR(256) NOT NULL
-- If the database or table already exist, the script will not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
