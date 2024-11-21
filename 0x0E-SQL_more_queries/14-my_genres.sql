-- Select the genre name from the tv_genres table
SELECT tv_genres.name
FROM tv_genres
-- Join the tv_show_genres table to link genres to the shows
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Join the tv_shows table to get the show with the title 'Dexter'
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
-- Filter the result to include only the genres for the show 'Dexter'
WHERE tv_shows.title = 'Dexter'
-- Sort the results by genre name in ascending order
ORDER BY tv_genres.name ASC;
