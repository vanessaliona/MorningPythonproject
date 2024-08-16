import sqlite3

conn = sqlite3.connect("example.db")
print("successfully connected")

conn.execute("INSERT INTO Employee VALUES(11, 'Mark','Mugo',45,120000.00, 'Manager')")
conn.execute("INSERT INTO Employee VALUES(21, 'Vee','Mwayuli',30,8000.00, 'Admin')")
conn.execute("INSERT INTO Employee VALUES(31, 'Frank','willbrand',20,12000.00, 'HR')")
conn.execute("INSERT INTO Employee VALUES(41, 'jane','Maina',25,12000.00, 'Receptionist')")
conn.execute("INSERT INTO Employee VALUES(51, 'Mike','Mwangi',18,12000.00, 'Marketter')")

conn.commit()
print("successfully inserted values into the Employee table")