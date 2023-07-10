from flask import Flask, render_template, request
from movements import getMovements, montoTotal
from transfer import postTransfer
import asyncio

app = Flask(__name__)

@app.route('/')
def index() :
    movements=getMovements()
    loop = asyncio.new_event_loop()
    total = loop.run_until_complete(montoTotal(movements))
    loop.close()
    return render_template('dashboard.html', movements=movements, total=total)

@app.route('/balance')
def balance():
    return render_template('pages/balance.html')

@app.route('/account')
def account():
    return render_template('pages/account.html')

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    print(request.method)
    if request.method == 'POST':
        nombre = request.form['nombre']
        monto = request.form['monto']
        loop = asyncio.new_event_loop()
        save = loop.run_until_complete(postTransfer(monto, nombre))
        loop.close()
        return render_template('pages/transfer.html', save=save)
    else:
        return render_template('pages/transfer.html')

if __name__=="__main__":
    app.run(debug=True)