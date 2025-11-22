from flask import Flask, request, jsonify, render_template
from predict import predict_image
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]
    img_path = "uploads/" + file.filename
    file.save(img_path)

    result = predict_image(img_path)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
