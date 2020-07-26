from django import forms
from .models import Taskdb

class TaskForm(forms.ModelForm):
    class Meta:
        model=Taskdb
        fields=['name','opinion']
