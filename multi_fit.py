import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.externals import joblib

csv_file_name = './data/home_insurance_final.csv'
print('Reading CSV: ' + csv_file_name)
df = pd.read_csv(csv_file_name)

# 85 features...
"""
Keepers - to be answered by insured

Generators - to be defaulted by the machine
"""

print('Dropping the junk...')
# Take out the trash....
df.drop(['LAST_ANN_PREM_GROSS'], axis=1, inplace=True)

# Round every value to integer
df_round = df.round(0)

def run_models(df):
    for col in df.columns:
        y = df[col]
        X = df.loc[:, df.columns != col]

        print('Splitting the data...')
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4)

        print('Building the model with ' + col + ' as the target...')
        # Train Decision Tree Classifer
        model = DecisionTreeClassifier(random_state=0)
        model = model.fit(X_train,y_train)

        print('Using the model for preditions...')
        #Predict the response for test dataset
        y_pred = model.predict(X_test)

        print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
        print("Saving the model to disk...")
        file_name = './models/' + col + '.joblib'
        joblib.dump(model, file_name)

print('Calling run_models')
run_models(df_round)
