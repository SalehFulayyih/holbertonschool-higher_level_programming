-- Script to list all genres and count the number of shows linked to each genre
-- Only genres with at least one linked show will be displayed
-- Results are sorted by number_of_shows in descending order
-- Output columns: genre, number_of_shows

-- Script to list all genres and count the number of shows linked to each genre
-- Only genres with at least one linked show will be displayed
-- Results are sorted by number_of_shows in descending order
-- Output columns: genre, number_of_shows

SELECT
  name AS genre,
  COUNT(*) AS number_of_shows
FROM
  tv_genres
JOIN
  tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY
  tv_show_genres.genre_id
ORDER BY
  number_of_shows DESC;

