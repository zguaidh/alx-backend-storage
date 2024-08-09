-- Created a stored procedure ComputeAverageWeightedScoreForUser that calculates and stores the average weighted score for a specific user
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN in_user_id INT)
BEGIN
    DECLARE weighted_avg FLOAT;

    SELECT SUM(c.score * p.weight) / SUM(p.weight) INTO weighted_avg
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = in_user_id;

    UPDATE users SET average_score = weighted_avg WHERE id = in_user_id;
END //

DELIMITER ;

