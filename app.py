
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
import random
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

DATA_PATH = os.path.join(os.path.dirname(__file__), 'recipe.csv')
df = pd.read_csv(DATA_PATH)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files.get("ingredientImage")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    # Random mock prediction
    selected_index = random.randint(0, len(df) - 1)
    dish = df.iloc[selected_index]

    return jsonify({
        "name": dish["Name"],
        "ingredients": dish["Ingredients"],
        "procedure": dish["Procedure"],
        "serving": dish["Serving"],
        "image": f"https://placehold.co/400x300/png?text={dish['Name'].replace(' ', '+')}&font=roboto"
    })

if __name__ == "__main__":
    app.run(debug=True)
