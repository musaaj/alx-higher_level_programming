-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT
    a.title
FROM
    tv_shows a
    INNER JOIN tv_show_genres b ON b.show_id = a.id
    INNER JOIN tv_genres c ON c.id = b.genre_id
WHERE
    c.name = "Comedy"
GROUP BY
    a.title
ORDER BY
    a.title ASC;
