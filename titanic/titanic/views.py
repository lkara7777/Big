from django.shortcuts import render
from . import model

from . import modelhr
import sys
import traceback
from decimal import Decimal


def welcome(request):
    return render(request,'home.html')
def hr(request):
    return render(request,'hr.html')
def hranalysismore(request):
    return render(request,'hranalysismore.html')
def hrranalysis(request):
    return render(request,'hrranalysis.html')
def index(request):
    return render(request,'index.html')
def sigmoid(request):
        return render(request,'sigmoid.html')
def result(request):

    NoTests=int(request.GET['NoTests'])

    country=request.GET['country']
    agegroup=request.GET['agegroup']
    type=str(request.GET['type'])
    gender=str(request.GET['gender'])
    promo=str(request.GET['promo'])
    trainer=str(request.GET['trainer'])
    #title=int(request.GET['title'])
    prediction=model.predict(NoTests,agegroup,country,type,gender,promo,trainer)
    prediction=prediction
    return render(request,'result.html',{'prediction':prediction})
    #except Exception as e:
        #print(e.message)


    # Get current system exception
def hrresult(request):
    #try:
    projects=int(request.GET['projects'])

    monthlyhours=int(request.GET['monthlyhours'])
    years=int(request.GET['years'])
    accidents=int(request.GET['accidents'])
    promotions=int(request.GET['promotions'])
    department=str(request.GET['department'])
    salary=str(request.GET['salary'])
    satisfaction=Decimal(request.GET['satisfaction'])

    evaluation=Decimal(request.GET['evaluation'])

    #title=int(request.GET['title'])
    prediction=modelhr.predict(projects,monthlyhours,years,accidents,promotions,department,salary,satisfaction,evaluation)
    prediction=prediction
    return render(request,'hrresult.html',{'prediction':prediction})
