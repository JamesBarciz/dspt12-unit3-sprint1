import pandas as pd
from time import sleep


df = pd.DataFrame([[1, 4, 6], [2, 4, 5], [1, 1, 0]])

while 1 == 1:
    sleep(2)
    df = pd.DataFrame([df.std()]) + 1
    print(df.head())
