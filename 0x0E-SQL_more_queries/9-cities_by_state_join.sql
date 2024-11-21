-- Select the id and name of cities, and the name of the corresponding state
SELECT cities.id, cities.name AS city_name, states.name AS state_name
FROM cities
-- Join the cities table with the states table based on the state_id
JOIN states ON cities.state_id = states.id
-- Sort the results by city id in ascending order
ORDER BY cities.id ASC;
