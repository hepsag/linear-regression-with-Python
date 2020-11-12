import pandas as pd
import statsmodels.api as sm
data = pd.read_excel('canada.xlsx')
df = pd.DataFrame(data, columns= ['interest','inflation'])
X = df["inflation"]
y = df["interest"]
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
results.summary()
print(results.summary())
