-- count distinct
-- SELECT DISTINCT score COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number
SELECT
    score,
    COUNT(*) AS number
FROM
    second_table
GROUP BY
    score
ORDER BY
    score DESC,
    number;
