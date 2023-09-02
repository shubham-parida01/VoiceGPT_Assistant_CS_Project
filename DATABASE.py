import mysql.connector

def save_prompt(prompt_text):

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='bhavya13jain'
    )

    cursor = connection.cursor()

    create_database_query = f"CREATE DATABASE IF NOT EXISTS COMMANDS_BY_USER"
    cursor.execute(create_database_query)

    cursor.execute(f"USE COMMANDS_BY_USER")

    create_table_query = """
        CREATE TABLE IF NOT EXISTS INPUTS_BY_USER (
            sno INT AUTO_INCREMENT PRIMARY KEY,
            prompt_text TEXT
        )
    """

    cursor.execute(create_table_query)

    insert_query = 'INSERT INTO INPUTS_BY_USER (prompt_text) VALUES (%s)'
    cursor.execute(insert_query, (prompt_text,))
    connection.commit()


