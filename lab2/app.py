from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/')
def home():
    # return jsonify({"message": "Witaj w moim API!"})
    return "Witaj w moim API!"

@app.route('/mojastrona')
def my_page():
    return "To jest moja strona!"

@app.route('/hello')
def hello_page():
    name = request.args.get('name')
    if name:
        return f"Hello {name}!"
    else:
        return "Hello!"

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    
    if num1 + num2 > 5.8:
        return jsonify({"prediction": 1, "features": {"num1": num1, "num2": num2}})
    else:
        return jsonify({"prediction": 0, "features": {"num1": num1, "num2": num2}})

if __name__ == '__main__':
    app.run()
