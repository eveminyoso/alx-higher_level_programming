-- Get genres linked to Dexter
CREATE TEMPORARY TABLE dexter_genres_temp AS
  SELECT DISTINCT tv_genres.id
  FROM tv_genres
  JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
  JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
  WHERE tv_shows.title = 'Dexter';

-- List genres not linked to Dexter
SELECT DISTINCT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (SELECT id FROM dexter_genres_temp)
ORDER BY tv_genres.name ASC;

-- Clean up temporary table
DROP TEMPORARY TABLE IF EXISTS dexter_genres_temp;
