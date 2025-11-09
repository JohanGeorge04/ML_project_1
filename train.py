
import pandas as pd
import numpy as np
import sklearn

import pickle

from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb

from sklearn.pipeline import make_pipeline



print(f'pandas=={pd.__version__}')
print(f'numpy=={np.__version__}')
print(f'sklearn=={sklearn.__version__}')


def load_data():

    df = pd.read_csv('diabetes_dataset.csv')

    del df['diabetes_stage']
    del df['diabetes_risk_score']

    return df



def train(df):

    y_train = (df.diagnosed_diabetes).astype('int').values
    del df['diagnosed_diabetes']

    train_dict = df.to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(train_dict)

    features = list(dv.get_feature_names_out())
    dtrain = xgb.DMatrix(X_train, label=y_train,
                    feature_names=features)
    
    xgb_params = {
    'eta': 0.1, 
    'max_depth': 4,
    'min_child_weight': 5,
    
    'objective': 'binary:logistic',
    'eval_metric': 'auc',

    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
    }

    model = xgb.train(xgb_params, dtrain, num_boost_round=150)

    return model,dv


def save_model(filename, model, dv):
    with open(filename, 'wb') as f_out:
        pickle.dump((model, dv), f_out)

df = load_data()
model, dv = train(df)
save_model('diabetes_model_xgb.bin', model, dv)

