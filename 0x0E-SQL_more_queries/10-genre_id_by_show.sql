-- list tv shows
SELECT
    title,
    b.genre_id
FROM
    tv_shows a
    INNER JOIN tv_show_genres b ON a.id = b.show_id
ORDER BY
    a.title,
    b.genre_id ASC;
