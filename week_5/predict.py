import pickle

with open('model1.bin', 'rb') as fh:
    model = pickle.load(fh)

with open('dv.bin', 'rb') as fh:
    dv = pickle.load(fh)

customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}
X = dv.transform([customer])
y_pred = model.predict_proba(X)[0, 1]
print(y_pred)

