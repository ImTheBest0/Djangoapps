from django import forms

class ToDoForm(forms.Form):
    name=forms.CharField(max_length=100)
    description=forms.CharField(widget=forms.Textarea)
    deadline=forms.DateTimeField()