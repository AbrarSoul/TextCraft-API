# app.py
from flask import Flask, request, jsonify
from model_wrapper import ModelWrapper

app = Flask(__name__)

# Initialize model
model = ModelWrapper()

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    max_length = data.get('max_length', 50)

    # Generate text using the model
    generated_text = model.generate_text(prompt, max_length)

    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
