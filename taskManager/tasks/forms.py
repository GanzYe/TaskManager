from django import forms
from django.contrib.auth.models import User
from tasks.models import Tasks


class TasksForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TasksForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['author'].widget = forms.HiddenInput()
        self.fields['status'].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['placeholder'] = 'Task name'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'

    class Meta:
        model = Tasks
        fields = '__all__'