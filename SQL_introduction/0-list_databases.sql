-- 0-list_databases.sql: list all current databases alphabetically

SELECT SCHEMA_NAME AS `Database`
FROM INFORMATION_SCHEMA.SCHEMATA
ORDER BY SCHEMA_NAME;