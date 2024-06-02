SELECT
    mc.country_code,
    m.mountain_range,
    p.peak_name,
    p.elevation
FROM mountains_countries AS mc
    JOIN mountains AS m
        ON mc.mountain_id = m.id
            JOIN peaks AS p
                ON m.id = p.mountain_id
WHERE country_code = 'BG'
AND
    p.elevation > 2835
ORDER BY
    p.elevation DESC