from flask import Flask
from flaskext.mysql import MySQL
import asyncio

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_BD']='poo'
mysql.init_app(app)

def getMovements() :
    sql = "SELECT * FROM poo.movements;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    movements=cursor.fetchall()

    return movements

async def montoTotal(movements) :
    await asyncio.sleep(1)
    total = 0
    for movement in movements:
        total += movement[2]
    return total