import customtkinter as ctk
import pymysql

connection = None

try:
    connection = pymysql.connect(
        host= 'localhost',
        port= 3306,
        user= 'root',
        password= '',
        database='mcrm'
    )

    if connection:
        print("Connected to the database !")
except pymysql.Error as error:
    print("Error while connecting to MySQL", error)
finally:
    if connection:
        connection.close()