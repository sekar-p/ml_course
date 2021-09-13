```python
import pandas as pd
import numpy as np
```


```python
pd.__version__
```




    '1.3.3'




```python
np.__version__
```




    '1.21.2'




```python
df = pd.read_csv('data.csv')
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Make</th>
      <th>Model</th>
      <th>Year</th>
      <th>Engine Fuel Type</th>
      <th>Engine HP</th>
      <th>Engine Cylinders</th>
      <th>Transmission Type</th>
      <th>Driven_Wheels</th>
      <th>Number of Doors</th>
      <th>Market Category</th>
      <th>Vehicle Size</th>
      <th>Vehicle Style</th>
      <th>highway MPG</th>
      <th>city mpg</th>
      <th>Popularity</th>
      <th>MSRP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BMW</td>
      <td>1 Series M</td>
      <td>2011</td>
      <td>premium unleaded (required)</td>
      <td>335.0</td>
      <td>6.0</td>
      <td>MANUAL</td>
      <td>rear wheel drive</td>
      <td>2.0</td>
      <td>Factory Tuner,Luxury,High-Performance</td>
      <td>Compact</td>
      <td>Coupe</td>
      <td>26</td>
      <td>19</td>
      <td>3916</td>
      <td>46135</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BMW</td>
      <td>1 Series</td>
      <td>2011</td>
      <td>premium unleaded (required)</td>
      <td>300.0</td>
      <td>6.0</td>
      <td>MANUAL</td>
      <td>rear wheel drive</td>
      <td>2.0</td>
      <td>Luxury,Performance</td>
      <td>Compact</td>
      <td>Convertible</td>
      <td>28</td>
      <td>19</td>
      <td>3916</td>
      <td>40650</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BMW</td>
      <td>1 Series</td>
      <td>2011</td>
      <td>premium unleaded (required)</td>
      <td>300.0</td>
      <td>6.0</td>
      <td>MANUAL</td>
      <td>rear wheel drive</td>
      <td>2.0</td>
      <td>Luxury,High-Performance</td>
      <td>Compact</td>
      <td>Coupe</td>
      <td>28</td>
      <td>20</td>
      <td>3916</td>
      <td>36350</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BMW</td>
      <td>1 Series</td>
      <td>2011</td>
      <td>premium unleaded (required)</td>
      <td>230.0</td>
      <td>6.0</td>
      <td>MANUAL</td>
      <td>rear wheel drive</td>
      <td>2.0</td>
      <td>Luxury,Performance</td>
      <td>Compact</td>
      <td>Coupe</td>
      <td>28</td>
      <td>18</td>
      <td>3916</td>
      <td>29450</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BMW</td>
      <td>1 Series</td>
      <td>2011</td>
      <td>premium unleaded (required)</td>
      <td>230.0</td>
      <td>6.0</td>
      <td>MANUAL</td>
      <td>rear wheel drive</td>
      <td>2.0</td>
      <td>Luxury</td>
      <td>Compact</td>
      <td>Convertible</td>
      <td>28</td>
      <td>18</td>
      <td>3916</td>
      <td>34500</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Make'] == 'BMW'
```




    0         True
    1         True
    2         True
    3         True
    4         True
             ...  
    11909    False
    11910    False
    11911    False
    11912    False
    11913    False
    Name: Make, Length: 11914, dtype: bool




```python
df[df['Make'].str.upper() == 'BMW'].describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Engine HP</th>
      <th>Engine Cylinders</th>
      <th>Number of Doors</th>
      <th>highway MPG</th>
      <th>city mpg</th>
      <th>Popularity</th>
      <th>MSRP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>334.000000</td>
      <td>334.000000</td>
      <td>334.000000</td>
      <td>334.000000</td>
      <td>334.000000</td>
      <td>334.000000</td>
      <td>334.0</td>
      <td>334.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2014.347305</td>
      <td>326.907186</td>
      <td>5.958084</td>
      <td>3.161677</td>
      <td>29.245509</td>
      <td>20.739521</td>
      <td>3916.0</td>
      <td>61546.763473</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.387983</td>
      <td>105.681659</td>
      <td>1.728939</td>
      <td>0.988324</td>
      <td>10.257037</td>
      <td>13.136879</td>
      <td>0.0</td>
      <td>27982.682153</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1995.000000</td>
      <td>170.000000</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>18.000000</td>
      <td>10.000000</td>
      <td>3916.0</td>
      <td>4697.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2015.000000</td>
      <td>240.000000</td>
      <td>4.000000</td>
      <td>2.000000</td>
      <td>25.000000</td>
      <td>17.000000</td>
      <td>3916.0</td>
      <td>42300.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2016.000000</td>
      <td>300.000000</td>
      <td>6.000000</td>
      <td>4.000000</td>
      <td>28.000000</td>
      <td>20.000000</td>
      <td>3916.0</td>
      <td>51850.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2016.000000</td>
      <td>394.000000</td>
      <td>7.500000</td>
      <td>4.000000</td>
      <td>33.000000</td>
      <td>22.000000</td>
      <td>3916.0</td>
      <td>79725.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2017.000000</td>
      <td>600.000000</td>
      <td>12.000000</td>
      <td>4.000000</td>
      <td>111.000000</td>
      <td>137.000000</td>
      <td>3916.0</td>
      <td>141200.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_make_after_2015 = df[(df['Make'] == 'BMW') & (df['Year'] >= 2015) ]
```


```python
df_make_after_2015.isnull().sum()
```




    Make                 0
    Model                0
    Year                 0
    Engine Fuel Type     0
    Engine HP            0
    Engine Cylinders     0
    Transmission Type    0
    Driven_Wheels        0
    Number of Doors      0
    Market Category      0
    Vehicle Size         0
    Vehicle Style        0
    highway MPG          0
    city mpg             0
    Popularity           0
    MSRP                 0
    dtype: int64




```python
df.isnull().sum()
```




    Make                    0
    Model                   0
    Year                    0
    Engine Fuel Type        3
    Engine HP              69
    Engine Cylinders       30
    Transmission Type       0
    Driven_Wheels           0
    Number of Doors         6
    Market Category      3742
    Vehicle Size            0
    Vehicle Style           0
    highway MPG             0
    city mpg                0
    Popularity              0
    MSRP                    0
    dtype: int64




```python
df['Engine HP'].mean()
```




    249.38607007176023




```python
df['Engine HP'].fillna(df['Engine HP'].mean()).mean()
```




    249.38607007176023




```python
rr_cars = df[df['Make'].str.replace(' ','-').str.lower() == 'rolls-royce']
without_dup = rr_cars[['Engine HP', 'Engine Cylinders', 'highway MPG']].drop_duplicates()
X = without_dup.values
X
```




    array([[325.,   8.,  15.],
           [563.,  12.,  19.],
           [563.,  12.,  21.],
           [563.,  12.,  20.],
           [322.,  12.,  15.],
           [453.,  12.,  19.],
           [624.,  12.,  21.]])




```python
XTX = X.T
XTX
```




    array([[325., 563., 563., 563., 322., 453., 624.],
           [  8.,  12.,  12.,  12.,  12.,  12.,  12.],
           [ 15.,  19.,  21.,  20.,  15.,  19.,  21.]])




```python
X.sum()
```




    3623.0




```python
m_X = XTX.dot(X)
m_X
```




    array([[1.754801e+06, 3.965600e+04, 6.519600e+04],
           [3.965600e+04, 9.280000e+02, 1.500000e+03],
           [6.519600e+04, 1.500000e+03, 2.454000e+03]])




```python
inv_res = np.linalg.inv(m_X)
inv_res.sum()
```




    0.03221232067748617




```python
element = [1000, 1100, 900, 1200, 1000, 850, 1300]
y = np.array(element)
temp = inv_res.dot(XTX)
w = temp.dot(y)
w
```




    array([ 0.19989598, 31.02612262, 31.65378877])


