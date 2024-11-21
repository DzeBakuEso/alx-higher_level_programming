-- 6-states.sql

-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create the table if it doesn't already exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- id is unique, auto-generated, not null, and primary key
    name VARCHAR(256) NOT NULL          -- name cannot be null
);
