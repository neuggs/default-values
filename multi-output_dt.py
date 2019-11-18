import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor

#csv_file_name = './data/home_insurance_final.csv'
csv_file_name = './data/home_insurance_final_small.csv'
print('Reading CSV: ' + csv_file_name)
df = pd.read_csv(csv_file_name)

print('Dropping the junk...')
# Take out the trash....
df.drop(['LAST_ANN_PREM_GROSS'], axis=1, inplace=True)

# Round every value to integer
df_round = df.round(0)

y1 = df['MAX_DAYS_UNOCC']
y2 = df['NCD_GRANTED_YEARS_C']
y3 = df['Gen_APPR_LOCKS']
y = pd.concat([y1, y2, y3], axis=1)

X = df.loc[:, (df.columns != 'MAX_DAYS_UNOCC') & (df.columns != 'NCD_GRANTED_YEARS_C') &
              (df.columns != 'Gen_APPR_LOCKS')]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=4)

max_depth = 30
#regr_multirf = MultiOutputRegressor(DecisionTreeRegressor(random_state=0))
regr_multirf = MultiOutputRegressor(RandomForestRegressor(n_estimators=100,
                                                          max_depth=max_depth,
                                                          random_state=0))
regr_multirf.fit(X_train, y_train)

# Predict on new data
y_multirf = regr_multirf.predict(X_test)

print('MultiOutputRegressor Predicted Values...')
print('Predicted y values: \n', y_multirf[:, 0], y_multirf[:,1], y_multirf[:,2])
print('Multi Score...')
print(regr_multirf.score(X_test, y_test))