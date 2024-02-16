-- lists all genres of the show Dexter
SELECT g.name
FROM tv_shows AS s INNER JOIN tv_show_genres AS sh ON s.id = sh.show_id
INNER JOIN tv_genres AS g ON sh.genre_id = g.id
WHERE s.title = 'Dexter'
ORDER BY g.name;
