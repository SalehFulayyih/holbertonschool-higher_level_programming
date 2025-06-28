-- This script creates the table 'unique_id' with:
-- id INT with default value 1 and a UNIQUE constraint
-- name VARCHAR(256)
-- The table is created only if it does not already exist

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
