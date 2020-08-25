from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):  # here TaskForm=name of model + ending with Form
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Add a new task...'}))

    class Meta:
        model = Task
        fields = '__all__'
