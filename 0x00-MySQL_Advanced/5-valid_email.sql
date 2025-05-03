-- This script creates a trigger that resets the attribute valid_email
-- only when the email has been changed.

DELIMITER //

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  -- Check if the email has been changed
  IF OLD.email <> NEW.email THEN
  -- Reset the valid_email field if the email is updated
      SET NEW.valid_email = 0
  ELSE
      SET NEW.valid_email = NEW.valid_email;
  END IF;
END;
//

DELIMITER ;

