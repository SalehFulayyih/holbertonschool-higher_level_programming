-- 12-no_cheating.sql :updates score of Bob to 10 without using id

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
