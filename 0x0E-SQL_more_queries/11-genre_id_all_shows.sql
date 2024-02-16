-- list all show in the database
-- Lists all the tvshows in the DB
SELECT title, genre_id
FROM tv_shows AS s LEFT OUTER JOIN tv_show_genres AS g
ON s.id=g.show_id
ORDER BY s.title, g.genre_id;
