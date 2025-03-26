from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Yiria Vaz":"5610599991", "Josue Perez" : "55555555555", "Jaime Rodriguez" : "1234567823", "James Bond" : "12345678909"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
