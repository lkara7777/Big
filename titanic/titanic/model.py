def predict(NoTests,agegroup,country,type,gender,promo,trainer):
    import pickle
    #from sklearn.externals import joblib
    if country=='Albania':
        country=2
    elif country=='Belgium':
        country=20
    elif country=='United Kingdom':
        country=218
    elif country=='USA':
        country=221
    elif country=='Greece':
        country=88
    elif country=='Cyprus':
        country=58
    elif country=='France':
        country=76
    elif country=='China':
        country=45
    elif country=='Germany':
        country=83

    if gender=='Male':
        gender=0
    elif gender=='Female':
        gender=1

    if type=='B2C':

        type=0
    elif type=='B2B':
        type=1

    if trainer=='No':
        trainer=0
    elif trainer=='Yes':
        trainer=1
    if promo=='No':
        promo=0
    elif promo=='Yes':
        promo=1
    if agegroup=='30-':
        agegroup=0
    elif agegroup=='30-40':
        agegroup=1
    elif agegroup=='40-50':
        agegroup=2
    elif agegroup=='50+':
        agegroup=3
    x=[[NoTests,agegroup,country,type,gender,promo,trainer]]
    randomforest=pickle.load(open('forestmodel.sav','rb'))
    #randomforest=pickle.load("randomforestmodel.sav")
    prediction=randomforest.predict(x)
    if prediction==0:
        prediction='IT'
        prediction=prediction+", this means that you can try: IT 5, IT courses."
    elif prediction==1:

        prediction='LANGUAGES'
        prediction=prediction+", this means that you can try: Turk,CITY,Pro,ES,IE,ES,S courses."



    elif prediction==2:
        prediction='OTHER'

        prediction=prediction+", this means that you can try:\n L,D,FUN,E,Computer Skills,I,Service,C,AM,CO,EC,DEV,COD,HOTEL courses."
        #prediction=prediction+", this means that you can try:\n LSS,DMI,FUNDED,LEAN IT,Computer Skills,INSETE,Service Desk,COMPTIA,AMSIS,COBIT5ECDL,DEVOPS,CODING BOOTCAMP,HOTEL KEYS courses."
    elif prediction==3:
        prediction='PPM'
        #prediction=prediction+", this means that you can try:\n AgileSHIFT, \n RESILIA, PPM courses."
        prediction=prediction+", this means that you can try:\n A, \n R, P courses."
    else:
        prediction='error'
    return prediction
