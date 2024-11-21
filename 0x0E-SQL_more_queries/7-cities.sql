-- 7-cities.sql

-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create the table if it doesn't already exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- id is unique, auto-generated, not null, and primary key
    state_id INT NOT NULL,              -- state_id is a foreign key
    name VARCHAR(256) NOT NULL,         -- name cannot be null
    CONSTRAINT fk_state FOREIGN KEY (state_id) REFERENCES states(id) 
    ON DELETE CASCADE                  -- On delete cascade ensures that if a state is deleted, cities related to it are also deleted
);
