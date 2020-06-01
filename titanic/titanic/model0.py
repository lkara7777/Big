def predict(TestTaken,AgeGroup,Country,DaysPast,Type,Gender,PromoFound,Trainer):
    import pickle
    #from sklearn.externals import joblib
    #from keras.models import load_model
    from sklearn.preprocessing import StandardScaler


    if Gender=='Male':
        Gender=0
    elif Gender=='Female':
        Gender=1

    if Type=='B2C':

        Type=0
    elif Type=='B2B':
        Type=1

    if Trainer=='No':
        Trainer=0
    elif Trainer=='Yes':
        Trainer=1
    if PromoFound=='No':
        PromoFound=0
    elif PromoFound=='Yes':
        PromoFound=1
    if AgeGroup=='30-':
        AgeGroup=0
    elif AgeGroup=='30-40':
        AgeGroup=1
    elif AgeGroup=='40-50':
        AgeGroup=2
    elif AgeGroup=='50+':
        AgeGroup=3
    x=[[TestTaken,AgeGroup,Country,DaysPast,Type,Gender,PromoFound,Trainer]]
    itil3model=pickle.load(open('itil3.sav','rb'))
    #itil3model=joblib.load("itil3model.sav")
    #itil3model=load.model("itil3model.h5")


    prediction=itil3model.predict(x)
    if prediction==0:
        prediction='you are not thinking to move on with the next level'
        prediction=prediction+", but for you there is a discount coupon so as to think again."
    elif prediction==1:
        prediction='you are thinking to move on with the next level,'
        prediction=prediction+ ' so in order to finalize your decision, we offer a discount coupon.'


    else:
        prediction='error'
    return prediction
