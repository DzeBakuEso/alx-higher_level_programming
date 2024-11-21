-- Select the title of the show from the tv_shows table
SELECT tv_shows.title
FROM tv_shows
-- Join the tv_show_genres table with tv_shows based on the show_id
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Join the tv_genres table with tv_show_genres based on the genre_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Filter the results to only include shows where the genre is 'Comedy'
WHERE tv_genres.name = 'Comedy'
-- Sort the results by the title of the show in ascending order (A-Z)
ORDER BY tv_shows.title ASC;
