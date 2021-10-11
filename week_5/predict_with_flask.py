import pickle
from flask import jsonify
from flask import request
from flask import Flask

with open('model2.bin', 'rb') as fh:
    model = pickle.load(fh)

with open('dv.bin', 'rb') as fh:
    dv = pickle.load(fh)

app = Flask('predict')


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1552)
