import pickle
from flask import jsonify
from flask import request
from flask import Flask

with open('model.bin', 'rb') as fh:
    dv, model = pickle.load(fh)


app = Flask('predict')

@app.route('/predict', methods=['POST'])
def predict():
    laptop_detail = request.get_json()
    X = dv.transform([laptop_detail])
    y_pred = model.predict(X)[0]
    predicted_price = round(y_pred, 2)
    model_type = 'Lower End'

    if predicted_price > 1123:
        model_type = 'High End'

    result = {"Your Laptop is": model_type, "Predict Price": predicted_price}

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1552)
