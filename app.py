from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'msg': 'BC4M'})

@app.route('/health')
def health_check():
    return jsonify({'status': 'OK'})

@app.route('/', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)