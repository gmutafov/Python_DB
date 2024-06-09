SELECT
    a.name,
    CASE
        WHEN EXTRACT(HOUR FROM c.start) BETWEEN 6 AND 20 THEN 'Day'
        ELSE 'Night'
    END AS day_time,
    c.bill,
    cl.full_name,
    cr.make,
    cr.model,
    ca.name
FROM courses AS c
    JOIN clients AS cl
        ON c.client_id = cl.id
            JOIN cars AS cr
                ON c.car_id = cr.id
                    JOIN categories AS ca
                        ON cr.category_id = ca.id
                            JOIN addresses AS a
                                ON c.from_address_id = a.id
ORDER BY c.id;