-- 16-no_link.sql : lists all records where name is not NULL or empty, ordered by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
