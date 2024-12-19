-- Select the title of the show from the tv_shows table and the genre_id from the tv_show_genres table
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- Perform a LEFT JOIN on the tv_show_genres table, matching the show_id from tv_show_genres to the id in tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Sort the results by tv_shows.title in ascending order, and then by genre_id in ascending order
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;