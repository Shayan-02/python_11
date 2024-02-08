create table students(
	s_id int identity(1, 1),
	fullname nvarchar(40),
	sp_id varchar(10),
	born date,
	tel varchar(20) default 0,
	adress nvarchar(150) default N'خالی',
	start_year int not null,
	primary key(s_id, fullname, sp_id, start_year)
);

create table teachers(
	t_id int identity(1, 1),
	t_fullname nvarchar(40),
	tp_id varchar(10),
	tel varchar(20) default 0,
	dars nvarchar(20),
	primary key(t_id, t_fullname, tp_id, dars)
);

create table doroos(
	d_id int identity(1, 1),
	d_name nvarchar(20),
	typ nvarchar(20),
	erae int,
	primary key(d_id, d_name)
);

