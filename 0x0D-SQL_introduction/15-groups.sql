-- This script list the number of records for each score in the second_table, sorted by the number of records
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
