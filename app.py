from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Protocop látásközpont működik!"

@app.route('/vision', methods=['POST'])
def vision():
    data = request.json
    print("Kapott adat:", data)
    return {"status": "ok", "message": "Adat feldolgozva"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
