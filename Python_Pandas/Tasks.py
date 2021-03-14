
import numpy as np
import pandas as pd

#Task 1
ind = pd.date_range("20210101", periods=10)
col = 'A B C D E'.split()

np.random.seed(101)
dat = np.random.randint(0,100,(10,5))

df1 = pd.DataFrame(data=dat,index=ind,columns=col)
df1

# Task 2
df2 = pd.DataFrame({
    "A": 2.0,
    "B": pd.Timestamp("20200108"),
    "C": np.linspace(1,10,10),
    "D": pd.Categorical(["X","Y","X","X","Y","Y","Y","X","Y","X"]),
})
df2