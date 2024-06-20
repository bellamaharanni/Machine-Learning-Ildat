import joblib
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
import os

#dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = ''

model_meat_classification = dir_path+'model/e-nose_meat_classification_model.sav'
global classifier_meat
classifier_meat = joblib.load(model_meat_classification)

#model_meat_regression = dir_path+'model/e-nose_meat_regression_model.sav'
#global regressor_meat
#regressor_meat = joblib.load(model_meat_regression)

scaler_meat_dir = dir_path+'model/scaler_meat.sav'
#print('scaler_meat_dir:',scaler_meat_dir)
scaler_meat = joblib.load(scaler_meat_dir)
#print('scaler_meat:',scaler_meat)
# klasifikasi
#model_file = 'model/e-nose_meat_classification_model.sav'
data_file = pd.read_csv('dataset/dataset.csv')
features = data_file.loc[:,'MQ135':'Temperature'].values
#print('features:',features)
#print(data_file)
#label = data_file['class']

# melakukan feature scaling
#scaler = StandardScaler()
#scaler.fit(features)
#scaled_feature=scaler.transform(features)
scaled_feature = scaler_meat.transform(features)
#print('scaled_feature:',scaled_feature)

#loaded_model = joblib.load(model_file)
#print('model:',loaded_model)
result = classifier_meat.predict(scaled_feature)
#print('result:',result)
hasil = pd.DataFrame(result)
print(hasil)
hasil.to_csv('hasil.csv')
#print(label)
