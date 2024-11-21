-- Select all columns from the cities table
SELECT * 
FROM cities 
-- Filter the cities where the state_id matches the id of California
WHERE state_id = 
    -- Subquery to find the id of California from the states table
    (SELECT id FROM states WHERE name = 'California') 
-- Sort the result in ascending order based on the city id
ORDER BY id ASC;
