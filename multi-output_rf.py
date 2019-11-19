import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor

csv_file_name = './data/home_insurance_final.csv'
print('Reading CSV: ' + csv_file_name)
df = pd.read_csv(csv_file_name)

#y_names = ['RISK_RATED_AREA_B', 'NCD_GRANTED_YEARS_B', 'RISK_RATED_AREA_C', 'NCD_GRANTED_YEARS_C',  'ROOF_CONSTRUCTION',
#           'WALL_CONSTRUCTION', 'LISTED', 'OWNERSHIP_TYPE']

y_names = ['Gen_APPR_ALARM', 'Gen_FLOODING', 'Gen_NEIGH_WATCH', 'Gen_SAFE_INSTALLED', 'Gen_SEC_DISC_REQ',
               'Gen_SUBSIDENCE', 'Gen_APPR_LOCKS']

y = df[y_names]
x_cols = [col for col in df.columns if col not in y_names]
X = df[x_cols]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=4)

max_depth = 30
#regr_multirf = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=0))

regr_multirf = MultiOutputRegressor(RandomForestClassifier(n_estimators=100, max_depth=max_depth, random_state=0))
print('Fitting...')
regr_multirf.fit(X_train, y_train)

# Predict on new data
print('Predicting...')
y_multirf = regr_multirf.predict(X_test)

print('MultiOutputRegressor Predicted Values...')
print('Predicted y values: \n', y_multirf[:, 0], y_multirf[:,1], y_multirf[:,2])
print('Multi Predict Score...')
print(regr_multirf.score(X_test, y_test))

"""
Scores Log
==================================
[1] 11/18/2019:
About to predict default values for 15 y-values and 48 X-values...
Multi Predict Score...
0.0412226210299137

[2] 11/18/2019:
Removed the rounding and split categorical and continuous y-features
Multi Predict Score...
0.16969857379018863

[3] 11/18/2019:
Tried with the categorical y-features...ugh...
Multi Predict Score...
-0.1672495983167183
"""