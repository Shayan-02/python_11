use dbtest6;
CREATE TABLE tbluser (
	id int primary key,
	fname nvarchar(20),
	lname nvarchar(30),
	born nvarchar(10),
	pid nvarchar(10),
	tel nvarchar(20)
);

insert into tbluser values (
	3, N'محمد', N'سعیدی', '2000/06/03', '0025689756', '09123645789'
);

CREATE TABLE tblcustomer (
	id int primary key identity(1,1),
	fname nvarchar(20),
	lname nvarchar(30),
	born nvarchar(10),
	pid nvarchar(10),
	tel nvarchar(20)
);


insert into tblcustomer values (
	N'محمد', N'سعیدی', '2000/06/03', '0025689756', '09123645789'
);
