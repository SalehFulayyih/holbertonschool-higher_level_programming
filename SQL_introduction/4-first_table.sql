-- 4-first_table.sql: create table first_table if it doesn't exist

CREATE TABLE IF NOT EXISTS first_table (
  id INT,
  name VARCHAR(256)
);
