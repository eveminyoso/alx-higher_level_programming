-- Listing score and names from second_table
-- Scores listed are above or eq 10

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
