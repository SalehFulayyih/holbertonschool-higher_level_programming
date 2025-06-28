-- Script to list all genres and count the number of shows linked to each genre
-- Only genres with at least one linked show will be displayed
-- Results are sorted by number_of_shows in descending order
-- Output columns: genre, number_of_shows

-- Script to list all genres and count the number of shows linked to each genre
-- Only genres with at least one linked show will be displayed
-- Results are sorted by number_of_shows in descending order
-- Output columns: genre, number_of_shows

SELECT
    genres.name AS genre,                    
    COUNT(tv_show_genres.show_id) AS number_of_shows  
FROM
    genres
JOIN
    tv_show_genres ON genres.id = tv_show_genres.genre_id  
GROUP BY
    genres.name                               
HAVING
    number_of_shows > 0                       
ORDER BY
    number_of_shows DESC;
