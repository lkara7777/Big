from django.shortcuts import render,redirect
from .models import Taskdb
from .forms import TaskForm
from django.contrib import messages

# Create your views here.
def tell(request):
    if request.method =='POST':
        form=TaskForm(request.POST or NONE)
        if form.is_valid():

            form.save()
            all_items=Taskdb.objects.all()
            return render(request,'indext.html',{'all_items':all_items})
    else:

        all_items=Taskdb.objects.all()
        return render(request,'indext.html',{'all_items':all_items})
def delete(request,list_id):
    item=Taskdb.objects.get(pk=list_id)
    item.delete()
    return redirect('tell')

def opinions(request,pk_op):
    Taskdb.objects.get(id=pk_op)
