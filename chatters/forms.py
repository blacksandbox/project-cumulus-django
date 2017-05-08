from django import forms

from . import models

class ChatterModelForm(forms.ModelForm):
    
    content = forms.CharField(
        label='', 
        max_length=200, 
        widget=forms.Textarea(attrs={"class":"form-control", "placeholder": "BLAHBLAHBLAH"})
    )
    
    class Meta: 
        model = models.Chatter
        
        #you need these
        fields = [
            #"user",
            "content"
        ]
        #exclude = ['user']

    #validations
    # def clean_content(self, *args, **kwargs):
    #     content = self.cleaned_data.get("content")
    #     if content == "abc":
    #         raise forms.ValidationError("Cannot be 'abc'")
    #     return content
        
