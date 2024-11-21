-- Create user 'user_0d_1' if not already created
CREATE USER 'user_0d_1'@'localhost';

-- Grant all privileges to 'user_0d_1' on all databases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Create user 'user_0d_2' if not already created (add this if the user is missing)
CREATE USER 'user_0d_2'@'localhost';

-- Grant all privileges to 'user_0d_2' on all databases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- Retrieve the grants/privileges for 'user_0d_1'
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Retrieve the grants/privileges for 'user_0d_2'
SHOW GRANTS FOR 'user_0d_2'@'localhost';
