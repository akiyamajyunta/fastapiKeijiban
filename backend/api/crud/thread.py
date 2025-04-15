import mysql.connector


def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password="root",
        database="sample"
    )
    return conn


def create(user_name, content):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO threads
        (user_name , content)
    VALUES 
        (%s, %s);
    """

    values = (user_name, content)     

    cursor.execute(query,values)
    connection.commit()
    cursor.close()
    connection.close()


def get():
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT * FROM threads;"""
    cursor.execute(query)
    threads = cursor.fetchall()
    return threads
#threads はリスト



def delete(id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """DELETE FROM threads WHERE id = (%s);"""
    id = (id, )
    cursor.execute(query, id)
    connection.commit()
    cursor.close()
    connection.close()






