-- Lists all shows without the genre Comedy, sorted by title
-- Each record should display: tv_shows.title
-- The database name will be passed as an argument of the mysql command

SELECT title FROM tv_shows
WHERE id NOT IN (
    SELECT tv_shows.id
    FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY title;
