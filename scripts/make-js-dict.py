import pandas as pd

data = pd.read_csv('../data/vdot-to-time-coefficients.csv')
first_col = data.columns[0]
cols = data.columns[1:]

string = 'var dict = {\n'

for index, row in data.iterrows():
    string += '"' + str(row[first_col]) + '" : {'
    for col in cols:
        string += '"' + str(col) + '" : ' + str(row[col]) + ','
    string += '},\n'

string += '};'

print(string)
    