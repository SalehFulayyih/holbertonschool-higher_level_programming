-- This script lists all cities with their corresponding state names
-- Output columns: cities.id, cities.name, states.name
-- Sorted by cities.id ascending
-- Only one SELECT statement allowed

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
