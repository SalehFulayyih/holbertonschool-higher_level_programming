-- This script lists all cities in California (state name = 'California')
-- without using JOIN keyword
-- Results sorted by cities.id ascending

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
