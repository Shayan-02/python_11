import sqlite3

sql = """
CREATE TABLE `tbluser` (
  `u_id` int(11) NOT NULL,
  `u_name` varchar(30) DEFAULT NULL,
  `u_pid` varchar(10) NOT NULL,
  `u_tel` varchar(20) DEFAULT NULL
)
"""