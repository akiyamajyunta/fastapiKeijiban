import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="root",
    database="sample"
)

cursor = conn.cursor()

cursor.execute("""
INSERT INTO threads
		(user_name , content)
	VALUES 
		('aaaaa', 'hello');
""")
conn.commit()

cursor.execute("""SELECT id, user_name, content FROM threads""")

for th in cursor.fetchall():
    print(th)

print(conn.is_connected())
cursor.close()
conn.close()

