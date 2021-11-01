from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
import pandas as pd
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('mushrooms.csv')

# Format the column names
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace('-', '_')

# Remove the ? from stalk_root
df[df['stalk_root'] == '?'].stalk_root.value_counts()

df['stalk_root'] = df['stalk_root'].replace('?', np.nan)

# Fill the missing value with best mode of the dataset
df['stalk_root'].fillna(df['stalk_root'].mode()[0], inplace=True)

# Encode all the values to numerical value
encode = LabelEncoder()

for col in df.columns:
    df[col] = encode.fit_transform(df[col]).astype("float32")

# Remove the unnecessary column
df.drop("veil_type", inplace=True, axis=1)

# Split the data for further processing
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(
    df_full_train, test_size=0.25, random_state=1)

# Prepare the target values
y_train = df_train['class'].values
y_val = df_val['class'].values
y_test = df_test['class'].values

# Reset the index of the subaset
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

# Delete the target variable from training set
del df_train['class']
del df_val['class']
del df_test['class']

# one hot encoding technique
dv = DictVectorizer(sparse=False)
train_dicts = df_train.to_dict(orient='records')
X_train = dv.fit_transform(train_dicts)

val_dicts = df_val.to_dict(orient='records')
X_val = dv.transform(val_dicts)

model = RandomForestClassifier(
    criterion='entropy', random_state=0, n_estimators=65)

model.fit(X_train, y_train)

y_pred = model.predict_proba(X_train)[:, 1]
auc = roc_auc_score(y_train, y_pred)
print(auc)

with open("model.bin", 'wb') as fh:
    pickle.dump((dv, model), fh)
