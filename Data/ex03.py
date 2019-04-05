import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv("../Data/student",sep="::")
df = pd.read_csv("../Data/student",delimiter='::', engine='python')
print(df)
zzz