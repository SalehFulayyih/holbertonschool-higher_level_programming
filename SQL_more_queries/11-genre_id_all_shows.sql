-- List all shows with their genre_id (NULL if no genre linked)
-- Sort by title and genre_id ascending
-- Only one SELECT statement

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;