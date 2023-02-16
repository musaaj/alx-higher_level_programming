-- lists all genres of the show Dexter.
SELECT
    a.name
FROM
    tv_genres a
    INNER JOIN tv_show_genres b ON b.genre_id = a.id
    INNER JOIN tv_shows c ON c.id = b.show_id
WHERE
    c.title = "Dexter"
GROUP BY
    a.name
ORDER BY
    a.name ASC;
