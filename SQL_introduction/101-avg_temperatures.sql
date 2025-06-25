-- 101-avg_temperatures.sql: calculate average Fahrenheit temperature per city
-- ordered by temperature (descending).

SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;