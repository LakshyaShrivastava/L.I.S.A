import sqlite3

conn = sqlite3.connect("lisa.db")
cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null, 'OneNote', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE')"
# cursor.execute(query)
# conn.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null, 'YouTube', 'https://www.youtube.com/')"
# cursor.execute(query)
# conn.commit()

# name = " OneNote"
# cursor.execute(
#                 'SELECT path FROM sys_command WHERE name IN (?)', (name,)
#                 )
# results = cursor.fetchall()
# print(results)

# cursor.execute("DELETE FROM web_command")
# conn.commit()
# cursor.execute("DELETE FROM sys_command WHERE name = 'One Note'")
# conn.commit()