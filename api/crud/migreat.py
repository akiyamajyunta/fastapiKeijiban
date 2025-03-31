import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="root",
    database="sample"
)
print(conn.is_connected())

cursor = conn.cursor()

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS threads (
    id              INT            NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_name       VARCHAR(10)    NOT NULL,
    content         VARCHAR(140)   NOT NULL
);
""")

cursor.close()
conn.close()

# テーブルを作成する
# テーブルは id, user_name, content を含める
# すでにテーブルが存在する場合は作らないようにしたい
# cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
