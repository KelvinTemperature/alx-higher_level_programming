-- lists the number of records..
-- lists the number of records with the score in second_table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
