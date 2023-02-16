import sqlite3
conn = sqlite3.connect('emobilis.db')
print("oppened db successfully")

conn.execute("INSERT INTO Students(ID, NAME, AGE, SCHOOL) VALUES (1,'Lynton',18,'emobilis')")
conn.execute("INSERT INTO Students(ID, NAME, AGE, SCHOOL) VALUES (2,'Mark',17,'modcom')")
conn.execute("INSERT INTO Students(ID, NAME, AGE, SCHOOL) VALUES (3,'Ethan',18,'SDA')")
conn.execute("INSERT INTO Students(ID, NAME, AGE, SCHOOL) VALUES (4,'Ambrose',19,'petanns')")
conn.execute("INSERT INTO Students(ID, NAME, AGE, SCHOOL) VALUES (5,'Carlos',13,'ukasee')")
conn.execute("INSERT INTO Students(ID, NAME, AGE, SCHOOL) VALUES (6,'Beavon',20,'army')")

conn.commit()
print("records added successfully")
conn.close()

