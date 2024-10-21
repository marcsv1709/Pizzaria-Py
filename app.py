from flask import Flask, render_template, request
from views import criar_pedido

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tipo_pizza = request.form["tipo_pizza"]
        metodo_pagamento = request.form["metodo_pagamento"]
        resultado_pedido = criar_pedido(tipo_pizza, metodo_pagamento)
        return render_template("pedido.html", pedido=resultado_pedido)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
