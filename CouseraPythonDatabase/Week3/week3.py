week3.py
Implementing data model in tables

table:
- primary key
- logical key
- foreign key (the primary key in other linked table)

Step1:
Design logical model of data base

Step2:
Create physical data base (from the begining table)
CREATE TABLE Genre(
		id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name	TEXT
	)

CREATE TABLE Album(
		id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		artist_id	INTEGER,
		title	TEXT
	)

CREATE TABLE Track(
		id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		title	TEXT,
		album_id	INTEGER,
		genre_id	INTEGER,
		len INTEGER, rating INTEGER, count INTEGER
	)

Step3:
Insert data

insert into Artist (name) values ('Led Zapplin');
insert into Artist (name) values ('AD/DC')

insert into Album (title, artist_id) values ('Who Made Who',2);
insert into Album (title, artist_id) values ('IV',1)

insert into Track (title, rating, len, count, album_id, genre_id) values ('Black Dog',5,297,0,2,1);
insert into Track (title, rating, len, count, album_id, genre_id) values ('Stairway',5,482,0,2,1);
insert into Track (title, rating, len, count, album_id, genre_id) values ('About to Rock',5,313,0,1,2);
insert into Track (title, rating, len, count, album_id, genre_id) values ('Who Made Who',5,207,0,1,2);


Step4:
SELECT Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id = Artist.id
Join pick all the conbinations together






