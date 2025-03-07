import mysql.connector
from mysql.connector import Error


def connect_to_database(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


# 示例调用
connection = connect_to_database("39.104.48.145", "meng", "Meng2024", "xzs")






