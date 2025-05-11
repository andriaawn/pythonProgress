from flask import Flask, request, jsonify, send_from_directory
import time

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/submit', methods=['POST'])
def submit():
    time.sleep(3)  # Simulating processing delay
    return jsonify({"message": "Form submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
