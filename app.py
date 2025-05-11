from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/abi')
def abi():
    with open('contract_abi.json') as f:
        contract_abi = json.load(f)
    return jsonify(contract_abi)

if __name__ == '__main__':
    app.run(debug=True)