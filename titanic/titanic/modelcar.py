def predict(gender,age,salary,debt,worth):

    import pickle


    from sklearn.preprocessing import MinMaxScaler
    import tensorflow
    from tensorflow import keras
    from keras.models import Sequential
    from keras.layers import Dense
    import numpy as np

    x=[[gender,age,salary,debt,worth]]
    scaler = MinMaxScaler()
    xf= scaler.fit_transform(x)
    obj=scaler.fit(x)
    x = obj.inverse_transform(xf)

    scaler_y = MinMaxScaler()

    carmodel=pickle.load(open('cars.sav','rb'))

    prediction=carmodel.predict(x)
    pred= scaler_y.fit_transform(prediction)
    object=scaler_y.fit(prediction)
    prediction = object.inverse_transform(pred)
    #pred= scaler_y.fit_transform(prediction)
    #prediction = scaler_y.inverse_transform(prediction)
    #prediction = scaler_y.inverse_transform(prediction)

    #prediction="The predicted value of the car is "+ prediction +'.'
    return prediction
