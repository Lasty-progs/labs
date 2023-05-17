--Функция находящая предметы в определенный день
CREATE OR REPLACE FUNCTION schedule_for_the_day (daz int)
RETURNS TABLE(para int, subject varchar,room_numb varchar, name varchar) AS '
	SELECT Tt.start_time, S.name, Tt.room_numb, T.full_name
	FROM Timetable Tt, Subject S, Teacher T
	WHERE Tt.day = daz AND Tt.name_subject = S.name AND
		T.name_subject = S.name
	ORDER BY Tt.start_time;
' language sql;


	


