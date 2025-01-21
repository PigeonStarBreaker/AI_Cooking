# from flask import Flask, request, jsonify
# from flask_cors import CORS
#
# app = Flask(__name__)
# CORS(app)
#
# @app.route('/find_recipes', methods=['POST'])
# def find_recipes():
#     data = request.get_json()
#     ingredients = data.get('ingredients', [])
#
#     if not ingredients:
#         return jsonify(message="No ingredient"), 400
#
#     return jsonify(message="Food successfully generated"), 200
#
# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from gemini_ai import gemini_food_recommendation

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('frontEnd.html')

@app.route('/find_recipes', methods=['GET', 'POST'])
def find_recipes():
    if request.method == 'POST':
        # Ensure the Content-Type is application/json
        if not request.is_json:
            return jsonify(message="Content-Type must be application/json"), 400

        # Get JSON data from the request
        data = request.get_json()
        print(data)
        ingredients = data.get('ingredients', [])
        print(ingredients)

        if not ingredients:
            return jsonify(message="No ingredients provided"), 400

        # return jsonify(message="Food successfully generated with ingredients: " + ', '.join(ingredients)), 200
        return jsonify(message=gemini_food_recommendation(ingredients))
    # For GET requests, simply return a welcome message or similar
    return jsonify(message="Send a POST request to generate recipes")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
