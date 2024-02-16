-- Creates a user on the server
-- CReates User user_0d_1 on the server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'USER_0d_1_pwd';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
