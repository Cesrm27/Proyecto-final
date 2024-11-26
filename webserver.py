from flask import Flask, jsonify,render_template, request
app = Flask(__name__)

cuentas = []

@app.route('/')
def inicio():
    return render_template('inicio.html', cuentas=cuentas)

if __name__ == '__main__':
    app.run(debug=True)