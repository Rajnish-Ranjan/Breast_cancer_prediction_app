from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

api_url = "http://172.18.0.3:5000/predict"

@app.route('/', methods=['GET', 'POST'])
def index():
    features = [
        "radius_mean", "texture_mean", "perimeter_mean", "area_mean",
        "smoothness_mean", "compactness_mean", "concavity_mean",
        "concave_points_mean", "symmetry_mean", "fractal_dimension_mean",
        "radius_se", "texture_se", "perimeter_se", "area_se",
        "smoothness_se", "compactness_se", "concavity_se",
        "concave_points_se", "symmetry_se", "fractal_dimension_se",
        "radius_worst", "texture_worst", "perimeter_worst", "area_worst",
        "smoothness_worst", "compactness_worst", "concavity_worst",
        "concave_points_worst", "symmetry_worst", "fractal_dimension_worst"
    ]

    if request.method == 'POST':
        data = {}
        for feature in features:
            data[feature] = float(request.form[feature])
        
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps([data]), headers=headers)
        result = response.json()
        # result example - {'label': 'M', 'prediction': 1, 'status': 200}
        return render_template('index.html', features=features, result=result)

    return render_template('index.html', features=features, result=None)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5005)
    
