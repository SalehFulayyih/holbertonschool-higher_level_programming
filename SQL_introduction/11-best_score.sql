-- 11-best_score.sql : lists records with score >= 10, ordered by score descending, with header

SELECT 'score', 'name'
UNION ALL
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
