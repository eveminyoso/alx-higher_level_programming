-- Get the genre ID for Comedy
SET @comedy_genre_id := (SELECT id FROM tv_genres WHERE name = 'Comedy');

-- List shows without the genre Comedy
SELECT DISTINCT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL OR tv_show_genres.genre_id != @comedy_genre_id
ORDER BY tv_shows.title ASC;
