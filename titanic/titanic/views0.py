from django.shortcuts import render
from . import model0
from . import modelc
from . import modelcar
import sys
import traceback
from decimal import Decimal


def it(request):
    return render(request,'it.html')
def ann(request):
    return render(request,'ann.html')
def prophet(request):
    return render(request,'prophet.html')
def orders(request):
    return render(request,'orders.html')
def annresult(request):

    gender=int(request.GET['gender'])
    age=Decimal(request.GET['age'])
    salary=Decimal(request.GET['salary'])
    debt=Decimal(request.GET['debt'])
    worth=Decimal(request.GET['worth'])


    #title=int(request.GET['title'])
    prediction=modelcar.predict(gender,age,salary,debt,worth)
    return render(request,'annresult.html',{'prediction':prediction})

def analysis1(request):
    return render(request,'analysis1.html')
def result0(request):



    TestTaken=int(request.GET['TestTaken'])
    AgeGroup=str(request.GET['AgeGroup'])
    Country=int(request.GET['Country'])
    DaysPast=int(request.GET['DaysPast'])
    Type=str(request.GET['Type'])
    Gender=str(request.GET['Gender'])
    PromoFound=str(request.GET['PromoFound'])
    Trainer=str(request.GET['Trainer'])
    #title=int(request.GET['title'])
    prediction=model0.predict(TestTaken,AgeGroup,Country,DaysPast,Type,Gender,PromoFound,Trainer)
    return render(request,'result0.html',{'prediction':prediction})

    # Get current system exception
def analysis(request):
    return render(request,'analysis.html')

def analysis0(request):
    return render(request,'analysis0.html')
def analysisC(request):
    try:


        TestTaken=int(request.GET['TestTaken'])
        AgeGroup=str(request.GET['AgeGroup'])
        Country=int(request.GET['Country'])
        DaysPast=int(request.GET['DaysPast'])
        Type=str(request.GET['Type'])
        Gender=str(request.GET['Gender'])
        PromoFound=str(request.GET['PromoFound'])
        Trainer=str(request.GET['Trainer'])
    #title=int(request.GET['title'])
        prediction=modelc.predict(TestTaken,AgeGroup,Country,DaysPast,Type,Gender,PromoFound,Trainer)
        return render(request,'analysisC.html',{'prediction':prediction})
    except Exception as e:
        print("")
