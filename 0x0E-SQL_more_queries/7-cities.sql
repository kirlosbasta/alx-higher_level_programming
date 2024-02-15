-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT PRIMARY KEY,
    states_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (states_id) REFERENCES states(id));
