-- Select the genre name and the count of shows linked to each genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
-- Perform a LEFT JOIN with the tv_show_genres table, matching genre_id from tv_genres with genre_id in tv_show_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Group the results by genre name, as we want to count the number of shows per genre
GROUP BY tv_genres.name
-- Filter the results to only include genres that have at least one show linked to them (i.e., where the count > 0)
HAVING number_of_shows > 0
-- Sort the results by the number of shows linked to each genre in descending order
ORDER BY number_of_shows DESC;
