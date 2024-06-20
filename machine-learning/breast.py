import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

#dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = ''

model_breast_classification = dir_path+'model/breastcancer.sav'
global classifier_breast
classifier_breast = joblib.load(model_breast_classification)

scaler_breast_dir = dir_path+'model/scaler_breast.sav'
scaler_breast = joblib.load(scaler_breast_dir)

# Membaca data dari file Excel
data_file = pd.read_excel('dataset/breast-cancer.xlsx')

# Memastikan hanya kolom numerik yang diambil untuk fitur
# Misalkan kolom fitur adalah dari 'radius_mean' sampai 'fractal_dimension_mean'
features = data_file.loc[:,'radius_mean':'fractal_dimension_mean'].values

# Melakukan feature scaling
scaled_feature = scaler_breast.transform(features)

# Melakukan prediksi
result = classifier_breast.predict(scaled_feature)

# Menyimpan hasil ke file CSV
hasil = pd.DataFrame(result, columns=['Prediction'])
print(hasil)
hasil.to_csv('hasil.csv', index=False)
