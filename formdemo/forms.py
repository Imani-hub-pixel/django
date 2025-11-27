from django import forms

class InputForm(forms.Form):
    first_name=forms.CharField(label='First Name', max_length=100)
    last_name=forms.CharField(label='Last Name', max_length=100)
    roll_number=forms.IntegerField(help_text="Enter 6 digit roll number")
    password=forms.CharField(widget=forms.PasswordInput)