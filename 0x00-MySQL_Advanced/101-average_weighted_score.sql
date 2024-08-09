-- Creates a stored procedure ComputeAverageWeightedScoreForUsers that calculates and stores the average weighted score for all users in the database
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE current_user_id INT;
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN user_cursor;

    user_loop: LOOP
        FETCH user_cursor INTO current_user_id;
        
        IF done THEN
            LEAVE user_loop;
        END IF;

         SELECT SUM(c.score * p.weight) / SUM(p.weight) INTO weighted_avg
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = current_user_id;

        UPDATE users SET average_score = weighted_avg WHERE id = current_user_id;
    END LOOP;

    CLOSE user_cursor;
END //

DELIMITER ;

