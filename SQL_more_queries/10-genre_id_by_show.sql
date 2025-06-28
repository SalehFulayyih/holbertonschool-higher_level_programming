-- List all shows that have at least one linked genre
-- Display: tv_shows.title, tv_show_genres.genre_id
-- Sort ascending by title and genre_id
-- Only one SELECT statement allowed

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;