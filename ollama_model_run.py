from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    //data = request.json
    # Call the model using subprocess
    //result = subprocess.run(['ollama', 'run', 'llama:8b', '--input', data['input']], capture_output=True, text=True)
    return '<h1>This is working just fine</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
