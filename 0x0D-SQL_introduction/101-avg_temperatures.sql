-- Lists average temp by city ordered by temp
USE hbtn_0c_0;

SELECT city, AVG(temperature) AS average_temperature
FROM temperature_data
GROUP BY city
ORDER BY average_temperature DESC;
