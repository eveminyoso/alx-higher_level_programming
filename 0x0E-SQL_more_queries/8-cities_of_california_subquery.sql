-- Find the state_id for California
SET @california_state_id := (SELECT id FROM states WHERE name = 'California');

-- List all cities of California
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = @california_state_id
ORDER BY cities.id ASC;
