import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

car_df = pd.read_csv('cardata.csv', encoding='ISO-8859-1')
sns.pairplot(car_df)
plt.show()
X = car_df.drop(['Customer Name', 'Customer e-mail', 'Country', 'Car Purchase Amount'], axis = 1)
y = car_df['Car Purchase Amount']

from sklearn.preprocessing import MinMaxScaler

scaler_x = MinMaxScaler()
X_scaled = scaler_x.fit_transform(X)
y = y.values.reshape(-1,1)
scaler_y = MinMaxScaler()

y_scaled = scaler_y.fit_transform(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

import tensorflow.keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler

model = Sequential()
model.add(Dense(25, input_dim=5, activation='relu'))
model.add(Dense(25, activation='relu'))
model.add(Dense(1, activation='linear'))
model.summary()
model.compile(optimizer='adam', loss='mean_squared_error')
epochs_hist = model.fit(X_train, y_train, epochs=12, batch_size=25,  verbose=1, validation_split=0.2)
plt.figure(figsize=(10,7))
plt.plot(epochs_hist.history['loss'])
plt.plot(epochs_hist.history['val_loss'])

plt.title('Model Loss Progression During Training/Validation')
plt.ylabel('Training and Validation Losses')
plt.xlabel('Epoch Number')
plt.legend(['Training Loss', 'Validation Loss'])
plt.savefig('lossnew.png')
plt.show()
pickle.dump(model, open('cars.sav', 'wb'))
X_test_sample = np.array([[1,	48.12708462,	52682.06401,	12514.52029,	549443.5886]])
scaler_x = MinMaxScaler()
X_test_sample = scaler_x.fit_transform(X_test_sample)
print(X_test_sample)
#y = y.values.reshape(-1,1)
#scaler_y = MinMaxScaler()

#y_scaled = scaler_y.fit_transform(y)
y_predict_sample = model.predict(X_test_sample)

print(y_predict_sample)
print('Expected Purchase Amount=', y_predict_sample)
y_predict_sample_orig = scaler_y.inverse_transform(y_predict_sample)
print('Expected Purchase Amount=', y_predict_sample_orig)