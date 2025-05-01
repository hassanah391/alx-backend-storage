-- This script creates a table for users
-- users Table contains id, email, and name coloumns


-- Create users tables if not exist
CREATE TABLE IF NOT EXISTS users (
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255)
);

