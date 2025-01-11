from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/find_recipes', methods=['POST'])
def find_recipes():
    data = request.get_json()
    ingredients = data.get('ingredients', [])

    if not ingredients:
        return jsonify(message="No ingredient"), 400

    return jsonify(message="Food successfully generated"), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
