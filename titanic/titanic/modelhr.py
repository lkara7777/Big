def predict(projects,monthlyhours,years,accidents,promotions,department,salary,satisfaction,evaluation):
    import pickle
    #from sklearn.externals import joblib
    if department=='sales':
        department=0
    elif department=='accounting':
        department=1
    elif department=='hr':
        department=2
    elif department=='technical':
        department=3
    elif department=='support':
        department=4
    elif department=='management':
        department=5
    elif department=='IT':
        department=6
    elif department=='product_mng':
        department=7
    elif department=='marketing':
        department=8
    elif department=='RandD':
        department=9

    if salary=='low':
        salary=0
    elif salary=='medium':
        salary=1
    elif salary=='high':
        salary=2

    x=[[projects,monthlyhours,years,accidents,promotions,department,salary,satisfaction,evaluation]]
    hrmodel=pickle.load(open('hrmodel.sav','rb'))
    #randomforest=pickle.load("randomforestmodel.sav")
    prediction=hrmodel.predict(x)
    if prediction==0:
        prediction='The employee is not going to leave.'

    elif prediction==1:

        prediction='Unfortunately, the employee is going to leave, take action if you do not want to get his/her resignation.'



    else:
        prediction='error'
    return prediction
