-- This script creates the table 'force_name' with columns:
-- id INT
-- name VARCHAR(256) NOT NULL
-- The table will be created only if it does not already exist

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
