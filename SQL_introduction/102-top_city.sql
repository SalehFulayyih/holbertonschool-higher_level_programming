-- 102-top_city.sql: show top 3 cities avg temperature during July & August
-- July and August ordered by temperature (descending).

SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = '7' OR month = '8'
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;