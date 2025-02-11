import pymysql
from config.config import *


def destroy_data():
    
    yield 
    
    sqls=[SQL1,SQL2,SQL3]

    conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        charset=DB_CHARSET
    )
    cur = conn.cursor()
    for sql in sqls:
        cur.execute(sql)
    cur.close()
    conn.close()
    