from django import forms
from .models import pmodel,hmodel

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django import forms  
# from django.contrib.auth.models import User  
# from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField,CharField,IntegerField
from django.forms.forms import Form  



class pform(forms.ModelForm):
    class Meta:
        model = pmodel
        fields = "__all__"

class hform(forms.ModelForm):
    class Meta:
        model = hmodel
        fields = "__all__"


class SignUpForm(UserCreationForm):
    name = forms.CharField(label='name', min_length=2, max_length=150)
    # lname = forms.CharField(label='lname', min_length=2, max_length=150)
    # age = forms.CharField(label='age', min_length=1, max_length=150)
    username = forms.EmailField(label='username', min_length=5, max_length=150)
    # phno = forms.CharField(label='phno', min_length=1, max_length=150)
    password1 = forms.CharField(label='password1', min_length=1, max_length=150)  
    password2 = forms.CharField(label='password2', min_length=1, max_length=150)  
    
    # def username_clean(self):  
    #     username = self.cleaned_data['username'].lower()  
    #     new = User.objects.filter(username = username)  
    #     if new.count():  
    #         raise ValidationError("User Already Exist")  
    #     return username  
  
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username=username)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return username  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user( 
            self.cleaned_data['name'],  
            # self.cleaned_data['lname'],  
            # self.cleaned_data['age'],
            self.cleaned_data['username'],
            # self.cleaned_data['phno'],        
            self.cleaned_data['password1']  
        )  
        return user