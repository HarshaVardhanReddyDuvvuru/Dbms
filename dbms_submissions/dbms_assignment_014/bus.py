CREATE TABLE Movie(id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(50))
CREATE TABLE Theater(id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(50))
CREATE TABLE Audience(id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(50), gender VARCHAR(1), age int,movie_name VARCHAR(50),Theater_name VARCHAR(50), FOREIGN KEY (movie_name) REFERENCES Movie (name),FOREIGN KEY (Theater_name) REFERENCES Theater (name));
