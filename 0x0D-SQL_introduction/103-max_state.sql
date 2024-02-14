--displays average temperature..
--displays average temperature by city
SELECT state, MAX(value) AS max_temp 
FROM temperatures
GROUP BY state
LIMIT 3;
