UPDATE
	projects
SET
	name = UPPER(name)
RETURNING *;