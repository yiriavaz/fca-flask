from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    cris = Contacto("Cristian", "56565656560")
    lolita = Contacto("Lolita Cortez", "5656565656")
    iron = Contacto("Iron man", "15656565657")
    list = []
    list.append(cris)
    list.append(lolita)
    list.append(iron)
    return jsonify(results = list)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
