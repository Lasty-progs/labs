CREATE TABLE chair (id SERIAL PRIMARY KEY, numb varchar NOT NULL, decanat integer NOT NULL);

CREATE TABLE student_group (id SERIAL PRIMARY KEY, numb varchar NOT NULL, chair_id integer NOT NULL REFERENCES chair(id));

CREATE TABLE student (id SERIAL PRIMARY KEY, full_name varchar NOT NULL, passport varchar(10) NOT NULL,
 group_id integer REFERENCES student_group(id));

INSERT INTO chair (numb, decanat) VALUES ('ИТ', '224');
INSERT INTO chair (numb, decanat) VALUES ('СиСС', '222');

INSERT INTO student_group (numb, chair_id) VALUES ('БВТ2201', '1');
INSERT INTO student_group (numb, chair_id) VALUES ('БВТ2202', '1');
INSERT INTO student_group (numb, chair_id) VALUES ('БИН2201', '2');
INSERT INTO student_group (numb, chair_id) VALUES ('БИН2202', '2');

INSERT INTO student (full_name, passport, group_id) VALUES ('Вася', '1234567890', '1');
INSERT INTO student (full_name, passport, group_id) VALUES ('Петя', '3251346650', '1');
INSERT INTO student (full_name, passport, group_id) VALUES ('Рома', '6541513213', '1');
INSERT INTO student (full_name, passport, group_id) VALUES ('Саша', '6436543545', '1');
INSERT INTO student (full_name, passport, group_id) VALUES ('Адам', '6842331235', '1');

INSERT INTO student (full_name, passport, group_id) VALUES ('Вика', '5342725467', '2');
INSERT INTO student (full_name, passport, group_id) VALUES ('Маша', '8975452163', '2');
INSERT INTO student (full_name, passport, group_id) VALUES ('Саша', '3548466854', '2');
INSERT INTO student (full_name, passport, group_id) VALUES ('Лера', '3854384848', '2');
INSERT INTO student (full_name, passport, group_id) VALUES ('Зина', '2457453733', '2');

INSERT INTO student (full_name, passport, group_id) VALUES ('Люба', '9854536143', '3');
INSERT INTO student (full_name, passport, group_id) VALUES ('Валя', '3457345757', '3');
INSERT INTO student (full_name, passport, group_id) VALUES ('Люда', '3457856788', '3');
INSERT INTO student (full_name, passport, group_id) VALUES ('Галя', '1234534266', '3');
INSERT INTO student (full_name, passport, group_id) VALUES ('Юлия', '7986586785', '3');

INSERT INTO student (full_name, passport, group_id) VALUES ('Ашот', '5453434453', '4');
INSERT INTO student (full_name, passport, group_id) VALUES ('Эрик', '1254533543', '4');
INSERT INTO student (full_name, passport, group_id) VALUES ('Гоша', '9634534553', '4');
INSERT INTO student (full_name, passport, group_id) VALUES ('Вова', '8734534534', '4');
INSERT INTO student (full_name, passport, group_id) VALUES ('Паша', '3788345325', '4');

SELECT * FROM chair;
SELECT * FROM student_group;
SELECT * FROM student;