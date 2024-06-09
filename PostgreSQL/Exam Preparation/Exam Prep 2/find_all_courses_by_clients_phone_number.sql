CREATE OR REPLACE FUNCTION fn_courses_by_client(phone_num VARCHAR(20))
RETURNS INT
AS
$$
DECLARE
    result INT;
BEGIN
    SELECT INTO result
    COUNT(cl.id)
FROM courses AS co
    JOIN clients AS cl
        ON co.client_id = cl.id
WHERE cl.phone_number = phone_num;
RETURN result;
END
$$
LANGUAGE plpgsql;

SELECT fn_courses_by_client('(803) 6386812')