select * from TblStudent as s
left join TblStCo sc on s.Stid = sc.StId
full join TEACHER t on TeachId = TeacherID
join TblCourse c on sc.CoID = c.CoID