-- This script create a procedure that computes and
-- store the average score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN in_user_id INT)
BEGIN
  DECLARE avg_score DECIMAL(10,2);
  -- Compute Average Score for a student from corrections table
  SELECT AVG(score) INTO avg_score
  FROM corrections
  WHERE user_id = in_user_id;

  -- Updates average_score of a student
  UPDATE users
  SET average_score = avg_score
  WHERE id = in_user_id;
END //

DELIMITER ;
