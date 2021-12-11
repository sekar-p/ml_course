import pickle
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import mutual_info_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import numpy as np
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('data.csv', encoding='latin1')

# Format the column names
df.columns = df.columns.str.lower()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].str.lower().str.replace('  ', ' ').str.replace(' ', '_')

df.rename(columns={'ram': 'ram_in_gb', 'weight': 'weight_in_kg', 'typename': 'type_name',
                   'screenresolution': 'screen_resolution', 'opsys': 'op_sys'}, inplace=True)

df['ram_in_gb'] = df['ram_in_gb'].str.replace('gb', '')

df['ram_in_gb'] = pd.to_numeric(df.ram_in_gb, errors='coerce')

df['weight_in_kg'] = df['weight_in_kg'].str.replace('kg', '')

df['weight_in_kg'] = pd.to_numeric(df.weight_in_kg, errors='coerce')

screen_split = df['screen_resolution'].str.split('x', expand=True)
df['y_res'] = screen_split[1]
df['x_res'] = screen_split[0].str.replace(',', '').str.findall(
    r'(\d+\.?\d+)').apply(lambda x: pd.Series(x).astype(int))

df['touch_screen'] = df['screen_resolution'].str.contains(
    'touchscreen').astype('int32')
df['screen_resolution_type'] = df['screen_resolution'].str.findall(
    r'(full_hd|4k)').apply(lambda x: pd.Series(x))

cpu_split = df['cpu'].str.split(
    r'(\d[\.\d]*)ghz').apply(lambda x: pd.Series(x))


df['processor'], df['clock_speed_ghz'] = cpu_split[0].str.strip('_'), cpu_split[1]

df['hard_disk_type'] = df.memory.apply(lambda x: 'hybrid' if (
    ('ssd' in x and 'hdd' in x) or 'hybrid' in x) else 'ssd' if 'ssd' in x else 'hdd')
memory_split = df['memory'].str.split('+', expand=True)
df['primary_memory'] = memory_split[0].str.findall(
    r'([\d\.]+[gb|tb]*)').apply(lambda x: pd.Series(x))[0]
df['primary_memory'] = df['primary_memory'].str.replace('1.0tb', '1tb')
df['primary_memory'].fillna('0gb', inplace=True)
df['primary_memory'] = df['primary_memory'].apply(lambda x:  int(x.replace(
    'tb', '')) * 1000 if 'tb' in x else int(x.replace('gb', '')) if 'gb' in x else int(x))
df['secondary_memory'] = memory_split[1].str.findall(
    r'([\d\.]+[gb|tb]*)').apply(lambda x: pd.Series(x))[0]
df['secondary_memory'] = df['secondary_memory'].str.replace('1.0tb', '1tb')
df['secondary_memory'].fillna('0gb', inplace=True)
df['secondary_memory'] = df['secondary_memory'].apply(lambda x:  int(x.replace(
    'tb', '')) * 1000 if 'tb' in x else int(x.replace('gb', '')) if 'gb' in x else int(x))
df['memory_gb'] = df['primary_memory'] + df['secondary_memory']

df = df.drop(['memory', 'primary_memory', 'secondary_memory',
              'screen_resolution'], axis=True)


# base feature(numerical + categorical)
features = df.columns

# Split the columns based on the value attribute
numerical = list(df.dtypes[df.dtypes != 'object'].index)
categorical = list(df.dtypes[df.dtypes == 'object'].index)

df['screen_resolution_type'].fillna('hd_ready', inplace=True)

# Split the data for further processing
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(
    df_full_train, test_size=0.25, random_state=1)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_full_train = df_full_train.reset_index(drop=True)

y_train = df_train.price_euros.values
y_val = df_val.price_euros.values
y_test = df_test.price_euros.values

del df_train['price_euros']
del df_val['price_euros']
del df_test['price_euros']

# one hot encoding technique
dv = DictVectorizer()

train_dict = df_train.to_dict(orient='records')
X_train = dv.fit_transform(train_dict)

val_dict = df_val.to_dict(orient='records')
X_val = dv.transform(val_dict)

test_dict = df_test.to_dict(orient='records')
X_test = dv.transform(test_dict)


model = RandomForestRegressor(n_estimators=55)
model.fit(X_train, y_train)

rf_pred = model.predict(X_val)

rf_score = model.score(X_val, y_val)
print(rf_score)

with open("model.bin", 'wb') as fh:
    pickle.dump((dv, model), fh)
