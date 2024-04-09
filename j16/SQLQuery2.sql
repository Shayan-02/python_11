create table stco(
	id int primary key identity(1, 1),
	grade int,
	stid bigint FOREIGN KEY REFERENCES TblStudent(Stid),
	tid int FOREIGN KEY REFERENCES TEACHER(TeachId)
);