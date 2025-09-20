from django import forms
from blog.models import comment
class commentform(forms.ModelForm):
    class Meta :
        model=comment
        fields=['name','email','subject','message','post']
