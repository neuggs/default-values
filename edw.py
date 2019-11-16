import pandas as pd
import pandas_profiling
from impyute.imputation.cs import mice
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

def read_ins_file(file_name):
    print('Reading the insurance file CSV ' + file_name + '...')
    df = pd.read_csv(file_name)
    return df

def clean_data(file_name):
    print('Cleaning the data...')
    df = pd.read_csv('./data/home_insurance.csv')
    print(df.columns)
    print(df.shape)

    df_clean = df[df.P1_EMP_STATUS.notnull() & df.BUS_USE.notnull() & df.AD_BUILDINGS.notnull()]
    df_clean.to_csv(file_name, index=False)

def impute_missing_vals(df, file_name):
    print("Starting imputing missing values...")
    imp = SimpleImputer(strategy="most_frequent")
    df[:] = imp.fit_transform(df)

    print("Shape after encoding booleans and imputing vals: ", df.shape)

    if file_name != None:
        df.to_csv(file_name, index=False)

    return df

def encode_booleans(df, file_name):
    print('Encoding booleans...')
    booleans = ['CLAIM3YEARS', 'BUS_USE', 'AD_BUILDINGS', 'AD_CONTENTS', 'CONTENTS_COVER', 'BUILDINGS_COVER',
                'P1_POLICY_REFUSED', 'P1_SEX', 'APPR_ALARM', 'APPR_LOCKS', 'FLOODING', 'NEIGH_WATCH', 'SAFE_INSTALLED',
                'SEC_DISC_REQ', 'SUBSIDENCE', 'LEGAL_ADDON_PRE_REN', 'LEGAL_ADDON_POST_REN', 'HOME_EM_ADDON_PRE_REN',
                'HOME_EM_ADDON_POST_REN', 'GARDEN_ADDON_PRE_REN', 'GARDEN_ADDON_POST_REN', 'KEYCARE_ADDON_PRE_REN',
                'KEYCARE_ADDON_POST_REN', 'HP1_ADDON_PRE_REN', 'HP1_ADDON_POST_REN', 'HP2_ADDON_PRE_REN',
                'HP2_ADDON_POST_REN', 'HP3_ADDON_PRE_REN', 'HP3_ADDON_POST_REN', 'MTA_FLAG'
                ]
    label_encoder = LabelEncoder()

    for house_var in booleans:
        gen_labels = label_encoder.fit_transform(df[house_var])
        new_col = 'Gen' + '_' + house_var
        df[new_col] = gen_labels

        # remove the column just encoded
        df.drop([house_var], axis=1, inplace=True)

    if file_name != None:
        df.to_csv(file_name, index=False)
    else:
        return df

def profile_data(df, file_name):
    print('Profiling the data...')
    profile = df.profile_report(title='Pandas Profiling Report')
    print('Saving the profile to HTML...')
    profile.to_file(output_file=file_name)

#clean_data('./data/home_insurance_rem_null.csv')
#df = read_ins_file('./data/home_insurance_rem_null.csv')
#profile_data(df, 'home_insurance_profile.html')

# Imputation
#df = read_ins_file('./data/home_insurance_rem_null.csv')
#df = encode_booleans(df, None)
#df = impute_missing_vals(df, './data/home_insurance_encoded_imputed.csv')

df = read_ins_file('./data/home_insurance_encoded_imputed.csv')
profile_data(df, 'home_insurance_encoded_imputed_profile.html')



