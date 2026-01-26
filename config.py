import os
import pymysql

DB_CONFIG = {
    'host': os.getenv('MCRM_DB_HOST') or 'localhost',
    'port': os.getenv('MCRM_DB_PORT') or 3306,
    'user': os.getenv('MCRM_DB_USER') or 'root',
    'password': os.getenv('MCRM_DB_PASSWORD') or '',
    'database': os.getenv('MCRM_DB_DATABASE') or 'mcrm'
}

def get_connection():
    connection = None
    try:
        connection = pymysql.connect(
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )

        return connection
    except pymysql.Error as err:
        print("Error while connecting to MySQL", err)