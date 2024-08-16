import sqlite3


conn = sqlite3.connect("example.db")
print("successfully connected")

conn.execute("""
CREATE TABLE Employee(
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT NOT NULL,
AGE INT,
SALARY REAL,
POSITION TEXT
)
""")

print("successfully")
conn.close()