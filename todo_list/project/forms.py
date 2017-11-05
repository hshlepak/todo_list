from django import forms
from django.forms import ModelForm
from .models import Task, Project


class TaskForm(forms.ModelForm):
    task_title = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Do something..'
        }
    ))
    task_day = forms.CharField(widget=forms.DateInput(
        attrs={
            'placeholder': 'YYYY-MM-DD'
        }
    ))
    task_time = forms.CharField(widget=forms.TimeInput(
        attrs={
            'placeholder': 'HH:MM:SS'
        }
    ))

    class Meta:
        model = Task
        fields = ['task_title', 'task_day', 'task_time', 'task_project']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_title']
