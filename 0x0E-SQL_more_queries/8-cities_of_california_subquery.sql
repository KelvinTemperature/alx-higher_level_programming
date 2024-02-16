-- Practice subquery
-- Query to get the cities of california
SELECT * FROM cities WHERE state_id = (
SELECT id FROM states WHERE name = "California");
