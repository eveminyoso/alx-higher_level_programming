-- Get shows with the genre Comedy
SET @comedy_shows := (SELECT DISTINCT tv_shows.id
                      FROM tv_shows
                      JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
                      JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
                      WHERE tv_genres.name = 'Comedy');

-- List shows without the genre Comedy
SELECT DISTINCT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (@comedy_shows)
ORDER BY tv_shows.title ASC;
