import numpy as np
import pandas as pd

x = np.random.rand(1000)
y = 3 + 5*x + 0.2*np.random.rand(1000)

df = pd.DataFrame({'x': x, 'y':y})
df.to_csv('./data/df.csv', index=False)