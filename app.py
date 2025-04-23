from flask import Flask, render_template, redirect, jsonify
import datetime
app = Flask(__name__)

pedidos = {
    'pedido': 0,
}

@app.route("/")
def pag_inicial():
    return render_template("index.html")

@app.route("/ligar/led")
def ligar_led():
    global pedidos
    pedidos = {
        'pedido': 1
    }
    return redirect("/")

@app.route("/apagar/led")
def desligar_led():
    global pedidos
    pedidos = {
        'pedido': 2
    }
    return redirect("/")

@app.route("/request")
def retorno_json():
    global pedidos
    return jsonify(pedidos)

if __name__:
    app.run(debug=True)