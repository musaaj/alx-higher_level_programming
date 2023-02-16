-- list cities found in a state
SELECT
    cities.id,
    cities.name,
    states.name
FROM
    cities
    JOIN states ON cities.state_id = states.id;
