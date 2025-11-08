import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3, np.nan, 7],
    'B': [np.nan, 2, np.nan, 8, 10]
})

# Interpolate using polynomial method of order 2, filling NaNs forward and backward, limiting to 1 consecutive NaN
df_interpolated = df.interpolate(method='polynomial', order=2, limit=1, limit_direction='both')

print(df_interpolated)