SELECT
    a.name AS animal,
    EXTRACT('year' FROM birthdate) AS birth_year,
    at.animal_type
FROM animals AS a
    JOIN animal_types AS at
        ON a.animal_type_id = at.id
WHERE AT.animal_type <> 'Birds'
    AND AGE('01/01/2022', a.birthdate) < '5 year'
    AND a.owner_id IS NULL
ORDER BY a.name