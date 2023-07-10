from flask import Flask
from flaskext.mysql import MySQL
import asyncio
from datetime import datetime

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_BD']='poo'
mysql.init_app(app)

async def postTransfer(monto, nombre) :
    detail = "transfetencia a "+nombre
    fecha_actual = datetime.now()
    date = fecha_actual.strftime("%Y-%m-%d")
    mont = -float(monto)
    sql = "INSERT INTO poo.movements (date, mont, detail) VALUES (%s, %s, %s)"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, (date, mont, detail))
    conn.commit()

    cursor.close()
    conn.close()
    await asyncio.sleep(1)

    return 'Datos guardados exitosamente'
