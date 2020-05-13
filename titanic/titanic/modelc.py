def predict(TestTaken,AgeGroup,Country,DaysPast,Type,Gender,PromoFound,Trainer):
    import pickle
    from sklearn.externals import joblib
    from keras.models import load_model
    from sklearn.preprocessing import StandardScaler



    if Country==88:
        Country='Greece'
    elif Country=='30-40':
        Country=1
    elif Country=='40-50':
        Country=2
    elif Country=='50+':
        Country=3

    #randomforest=pickle.load(open('randomforestmodel.pkl','rb'))
    #itil3model=joblib.load("itil3modelgr.sav")
    #itil3model=load.model("itil3model.h5")


    #prediction=itil3model.predict(x)
    if Country=='Greece':
        prediction='Data Analysis for Greece'

    elif prediction==1:
        prediction='you are thinking to move on with the next level,'



    else:
        prediction='error'
    return prediction
