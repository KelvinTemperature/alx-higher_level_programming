--lists all record of the table..
--lists all records of second_table with names
SELECT score, name FROM second_table
WHERE name IS NOT NULL 
ORDER BY score DESC;
