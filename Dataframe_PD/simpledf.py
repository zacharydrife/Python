import pandas as pd
import numpy as np

# Create a dataframe
df = pd.DataFrame({
    'Product ID': [1, 2, 3, 4],
    'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
    'Color': ['blue', 'green', 'red', 'black']
})

print(df)

# Alt df

df0 = pd.DataFrame([
    [1, 't-shirt', 'blue'],
    [2, 't-shirt', 'green'],
    [3, 'skirt', 'red'],
    [4, 'skirt', 'black']

    ], columns=['Product ID', 'Product Name', 'Color'])

print(df0)
