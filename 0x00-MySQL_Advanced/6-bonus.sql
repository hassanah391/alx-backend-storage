-- This script creates a stored procedure AddBonus that adds
-- a new correction for a student.
-- Requirements:
-- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a users.id value
-- project_name, a new or already exists projects - if no projects.name found
-- in the table, you should create it
-- score, the score value for the correction

DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
  DECLARE project_id INT;

  -- Declare a flag to detect if project exists
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET project_id = NULL;
  -- Try to get the project_id
  SELECT id INTO project_id FROM projects WHERE name = project_name;

  -- If not found, insert the project
  IF project_id IS NULL THEN
    INSERT INTO projects (name)
    VALUES(project_name);
    SET project_id = LAST_INSERT_ID();
  END IF;

  -- Insert correction, update if exists
  INSERT INTO corrections (user_id, project_id, score)
  VALUES(user_id, project_id, score)
  ON DUPLICATE KEY UPDATE score = score;

END;
//

DELIMITER ;
