from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import random

df = pd.read_csv("recipe.csv")


food_names = df['Name'].tolist()


app = Flask(__name__)
CORS(app) 

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files.get("ingredientImage")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

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
