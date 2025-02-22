-- 1-create_user.sql

-- Check if the user exists, if not, create the user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user on all databases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Make sure privileges are reloaded after the changes
FLUSH PRIVILEGES;
