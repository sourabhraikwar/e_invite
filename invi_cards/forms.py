from django import forms

class E_Form(forms.Form):
    
    title = forms.CharField(label='Enter the title', min_length=100, max_length=150)
    Firstname = forms.CharField(label='Enter firstname', min_length=40, max_length=50)
    Secondname = forms.CharField(label='Enter Secondname', min_length=40, max_length=50)