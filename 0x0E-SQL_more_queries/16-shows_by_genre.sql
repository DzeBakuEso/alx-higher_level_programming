-- Select the title of the TV show and its associated genre name
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
-- Perform a LEFT JOIN with tv_show_genres to get the genre links for each show
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Perform another LEFT JOIN with tv_genres to get the name of the genre for each linked genre_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Order the results first by the show title in ascending order, then by the genre name in ascending order
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
