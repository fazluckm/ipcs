from django import forms 
from .models import Contact

class UserForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','phone']
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter your name'}),
            'email':forms.EmailInput(attrs={'placeholder':"enter your email"}),
            'phone':forms.NumberInput(attrs={"placeholder":"enter your phone number"})
        }