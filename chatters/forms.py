from django import forms

from . import models

class ChatterModelForm(forms.ModelForm):
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
        
