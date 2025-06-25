-- 103-max_state.sql: display max Fahrenheit temperature per state, ordered by state


SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;