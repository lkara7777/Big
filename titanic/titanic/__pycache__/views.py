from django.shortcuts import render
from . import model
import sys
import traceback


def home(request):
    return render(request,'index.html')
def result(request):
    try:


        NoTests=int(request.GET['NoTests'])

        country=request.GET['country']
        agegroup=request.GET['agegroup']
        type=str(request.GET['type'])
        gender=str(request.GET['gender'])
        trainer=str(request.GET['trainer'])
    #title=int(request.GET['title'])
        prediction=model.predict(NoTests,agegroup,country,type,gender,trainer)
        return render(request,'result.html',{'prediction':prediction})
    except Exception as e:
        print(e.message)
    # Get current system exception
