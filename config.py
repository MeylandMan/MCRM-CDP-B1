import os

DB_CONFIG = {
    'host': os.getenv('MCRM_DB_HOST') or 'localhost',
    'port': os.getenv('MCRM_DB_PORT') or 3306,
    'user': os.getenv('MCRM_DB_USER') or 'root',
    'password': os.getenv('MCRM_DB_PASSWORD') or '',
    'database': os.getenv('MCRM_DB_DATABASE') or 'mcrm'
}