CREATE TABLE Subject(
name VARCHAR NOT NULL PRIMARY KEY
);

CREATE TABLE Timetable(
id BIGSERIAL NOT NULL PRIMARY KEY,
day INT
	CONSTRAINT wrong_day
	CHECK(day >0 AND
		day <15),
name_subject VARCHAR REFERENCES Subject,
room_numb VARCHAR NOT NULL,
start_time int
);

CREATE TABLE Teacher(
id BIGSERIAL NOT NULL PRIMARY KEY,
full_name VARCHAR NOT NULL,
name_subject VARCHAR REFERENCES Subject
);