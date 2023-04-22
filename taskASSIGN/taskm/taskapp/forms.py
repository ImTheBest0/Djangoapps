from django import forms
from .models import tasks

class tasksForm(forms.ModelForm):
    instructions = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,'class':'form-control col-md-3'}))
    class Meta:
        model=tasks
        fields=('name','description','workers','expected_date','deadline')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control col-md-3'}),
            'description':forms.Textarea(attrs={'class':'form-control col-md-7'}),
            'workers':forms.SelectMultiple(attrs={'class':'form-control col-md-3'}),
            'deadline':forms.DateTimeInput(attrs={'class':'form-control col-md-3','type':'datetime-local'}),
            'expected_date':forms.DateTimeInput(attrs={'class':'form-control col-md-3','type':'datetime-local'}),
            
        }
        
class answerForm(forms.ModelForm):
    detailsres=forms.CharField(
        label="Report",
        widget=forms.Textarea(
            attrs={'class':'form-control col-md-3'}
        )
    )
    resolutiondocs= forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,'class':'form-control col-md-3'}))
    class Meta:
        model=tasks
        fields=('detailsres','resolutiondocs')
    
