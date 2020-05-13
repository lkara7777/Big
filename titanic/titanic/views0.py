from django.shortcuts import render
from . import model0
from . import modelc
import sys
import traceback


def itil(request):
    return render(request,'itil.html')
def result0(request):
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
        prediction=model0.predict(TestTaken,AgeGroup,Country,DaysPast,Type,Gender,PromoFound,Trainer)
        return render(request,'result0.html',{'prediction':prediction})
    except Exception as e:
        print("")
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
