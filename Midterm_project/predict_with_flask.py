import pickle
from flask import jsonify
from flask import request
from flask import Flask

with open('model.bin', 'rb') as fh:
    dv, model = pickle.load(fh)


app = Flask('predict')

@app.route('/predict', methods=['POST'])
def predict():
    mushroom_data = request.get_json()

    X = dv.transform([mushroom_data])
    y_pred = model.predict_proba(X)[0, 1]
    edible = y_pred < 0.5

    result = {
        'edible_probability': float(y_pred),
        'edible': bool(edible)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1552)
