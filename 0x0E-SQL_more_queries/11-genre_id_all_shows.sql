-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT
    title,
    b.genre_id
FROM
    tv_shows a
    LEFT JOIN tv_show_genres b ON a.id = b.show_id
ORDER BY
    a.title,
    b.genre_id ASC;
