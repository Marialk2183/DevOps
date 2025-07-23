from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/api')
def api():
    return jsonify({"message": "Hello from API"})

if __name__ == '__main__':
    app.run(debug=True)
