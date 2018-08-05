#Week4_manyToMany.py

- Add a connection table with 2 foreign keys
- There is usaully no seperate primary key

> transfer to 2 one to many model

CREATE TABLE User(
		id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name	TEXT,
		email TEXT
	)
CREATE TABLE Course(
		id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name	TEXT
	)

CREATE TABLE Member (
		user_id		INTEGER,
		course_id	INTEGER,
		role		INTEGER,
		PRIMARY KEY (user_id, course_id)
		; 
	)


cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))