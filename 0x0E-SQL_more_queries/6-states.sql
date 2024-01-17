-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the created or existing database
USE hbtn_0d_usa;

-- Create table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
