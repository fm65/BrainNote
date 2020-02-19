DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS task;

CREATE DATABASE todolistdb;
use todolistdb;

CREATE TABLE user (
  id INT(11) AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL
);

CREATE TABLE task (
  id INT(11) AUTO_INCREMENT PRIMARY KEY,
  author_id INTEGER NOT NULL,
  content TEXT NOT NULL,
  done boolean DEFAULT false,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
