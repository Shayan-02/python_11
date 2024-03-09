import sqlite3

connection = sqlite3.Connection("./my-database.db")
cursor = connection.cursor()

sql = """
 CREATE TABLE IF NOT EXISTS user (
 s_id INTEGER ,
 s_name VARCHAR (60),
 s_family VARCHAR (60),
 s_email VARCHAR (60)
 );
"""

sql = """
 CREATE TABLE IF NOT EXISTS teacher (
 t_id INTEGER ,
 t_name VARCHAR (60),
 t_family VARCHAR (60),
 t_email VARCHAR (60)
 );
"""

sql = """
 CREATE TABLE IF NOT EXISTS student (
 s_id INTEGER ,
 s_name VARCHAR (60),
 s_family VARCHAR (60),
 s_email VARCHAR (60)
 );
"""

sql = """
 select * from student
"""

cursor.execute(sql)
connection.commit()
connection.close()