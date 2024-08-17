from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Call the model using subprocess
    result = subprocess.run(['ollama', 'run', 'llama:8b', '--input', data['input']], capture_output=True, text=True)
    return jsonify({'output': result.stdout})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
