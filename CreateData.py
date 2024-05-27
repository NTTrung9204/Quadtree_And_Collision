import numpy as np
import pandas as pd

X = np.random.randint(0, 1200, 10**5)
Y = np.random.randint(0, 800, 10**5)

df = pd.DataFrame({"X": X, "Y": Y})
df.to_csv("DataPoint.csv", mode='a', header=False, index=False)