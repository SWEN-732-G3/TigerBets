-- Drop table if it already exists
DROP TABLE IF EXISTS Users CASCADE;


-- Create table
CREATE TABLE Users (
    user_name varchar(100) PRIMARY KEY,
    password VARCHAR(128) NOT NULL,
    full_name varchar(500),
    email varchar(100),
    is_deleted BOOLEAN DEFAULT false);
