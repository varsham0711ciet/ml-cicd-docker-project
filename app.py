from flask import Flask, request, jsonify, render_template_string
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Small ML model trained from the built-in Iris dataset.
iris = load_iris()
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(iris.data, iris.target)

HTML = """
<!doctype html>
<html>
<head>
  <title>ML Iris Prediction</title>
  <style>
    body { font-family: Arial; max-width: 650px; margin: 50px auto; padding: 20px; }
    input { width: 100%; padding: 10px; margin: 7px 0; }
    button { padding: 12px 20px; }
    .result { margin-top: 20px; font-size: 20px; }
  </style>
</head>
<body>
  <h1>ML Iris Flower Prediction</h1>
  <p>Enter four flower measurements.</p>
  <form method="post">
    <input name="sepal_length" placeholder="Sepal length" required>
    <input name="sepal_width" placeholder="Sepal width" required>
    <input name="petal_length" placeholder="Petal length" required>
    <input name="petal_width" placeholder="Petal width" required>
    <button type="submit">Predict</button>
  </form>
  {% if result %}
    <div class="result">Prediction: <b>{{ result }}</b></div>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        values = [
            float(request.form["sepal_length"]),
            float(request.form["sepal_width"]),
            float(request.form["petal_length"]),
            float(request.form["petal_width"])
        ]
        result = iris.target_names[model.predict([values])[0]]
    return render_template_string(HTML, result=result)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    values = data["features"]
    prediction = int(model.predict([values])[0])
    return jsonify({
        "prediction": prediction,
        "flower": iris.target_names[prediction]
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
