-- Create a view that lists students with a score under 80 and either no last_meeting or a last_meeting more than one month ago
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));

