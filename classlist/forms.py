from django import forms
from .models import ClassList

class ClassListForm(forms.ModelForm):
    name=forms.CharField(max_length=100)
    admission_number=forms.IntegerField()
    label='Add Student'
    widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'admission_number':forms.NumberInput(attrs={'class':'form-control'}),
    }
    class Meta:
        model = ClassList
        fields = ['name', 'admission_number']
    