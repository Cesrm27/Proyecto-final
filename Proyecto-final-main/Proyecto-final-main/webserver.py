from flask import Flask, jsonify,render_template, request
app = Flask(__name__)

cuentas = []

@app.route('/')
def inicio():
    return render_template('inicio.html', cuentas=cuentas)

@app.route('/add_cuenta', methods=['POST'])
def add_account():
    gift_name = request.form.get('account_name')
    
    if account_name :
        cuentas.append({'gift_name': gift_name})
    
    return render_template('index.html', cuentas=cuentas)

@app.route('/get_descripcion', methods=['GET'])
def get_descripcion():
    gift_names = [get_descripcion['descripcion_name'] for gift in cuentas]
    return jsonify(descripcion_names)

if __name__ == '__main__':
    app.run(debug=True)