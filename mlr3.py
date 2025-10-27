# LINEAR REGRESSION
import pandas as pd
import statsmodels.api as sm

# LOAD DATA
df = pd.read_excel(
    r'C:\Users\sebas\Documents\Python\Python Projects\germany_gva\Data\processed\germany_gva_analysis.xlsx',
    sheet_name='schema_2'
)

# DEFINE VARIABLES
Y = df['2021 GDP (PPP) Per Capita USD']
X = df['2021 GVA Manufacturing']

# ADD INTERCEPT
X = sm.add_constant(X)

# FIT THE MODEL
model = sm.OLS(Y, X).fit()

# SHOW
print(model.summary())
