-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;

-- Use the newly created database
USE hbtn_0e_0_usa;

-- Create the `states` table with an auto-incrementing `id` and a `name`
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);

-- Insert example states into the `states` table
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
