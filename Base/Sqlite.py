__author__ = 'Administrator'
import sqlite3
class base_sqlite3:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.file = file
    def drop_table(self):
        self.conn.execute('DROP TABLE COMPANY')
        print("del database success!!")
    def create_sql(self):
        #创建在硬盘上面： conn = sqlite3.connect('c:\\test\\test.db')
        #创建在内存上面： conn = sqlite3.connect(':memory:')
        self.conn.execute('''CREATE TABLE COMPANY
               (ID INT PRIMARY KEY     NOT NULL,
               NAME           TEXT    NOT NULL,
               AGE            INT     NOT NULL,
               ADDRESS        CHAR(50),
               SALARY         REAL);''')
        print("Table created successfully")
        self.conn.close()

    def insert_sql(self):
        self.conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (1, 'Paul', 32, 'California', 20000.00 )")
        self.conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
        self.conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
        self.conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
        self.conn.commit()
        print("Records created successfully")
        self.conn.close()

    def select_sql(self):
        cursor = self.conn.execute("SELECT id, name, address, salary  from COMPANY")
        for row in cursor:
           print("ID = ", row[0])
           print("NAME = ", row[1])
           print("ADDRESS = ", row[2])
           print("SALARY = ", row[3], "\n")
        print("Operation done successfully")
        self.conn.close()
    def update_sql(self):
        self.conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
        self.conn.commit
        print("Total number of rows updated :", self.conn.total_changes)
        cursor = self.conn.execute("SELECT id, name, address, salary  from COMPANY")
        for row in cursor:
           print("ID = ", row[0])
           print("NAME = ", row[1])
           print("ADDRESS = ", row[2])
           print("SALARY = ", row[3], "\n")

        print("Operation done successfully")
        self.conn.close()
    def del_sql(self):

        self.conn.execute("DELETE from COMPANY where ID=2;")
        self.conn.commit
        print("Total number of rows deleted :", self.conn.total_changes)

        cursor = self.conn.execute("SELECT id, name, address, salary  from COMPANY")
        for row in cursor:
           print("ID = ", row[0])
           print("NAME = ", row[1])
           print("ADDRESS = ", row[2])
           print("SALARY = ", row[3], "\n")

        print ("Operation done successfully")
        self.conn.close()