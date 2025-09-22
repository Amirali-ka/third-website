from django import forms
from django.forms import ModelForm
from mywebsite.models import Contact,newsletter
from captcha.fields import CaptchaField
class nameform(forms.Form):
    name=forms.CharField(max_length=250)
    email=forms.EmailField()
    subject=forms.CharField(max_length=200)
    message=forms.CharField(widget=forms.Textarea)
class contactform(ModelForm):
    captcha = CaptchaField()
    class Meta :
        model=Contact
        fields='__all__'
class newsletterform(ModelForm):
    class Meta :
        model=newsletter
        fields='__all__'