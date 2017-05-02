from django.contrib import admin

# Register your models here.
from . import forms
from . import models

#admin.site.register(models.Chatter)

class ChatterModelAdmin(admin.ModelAdmin):
    #form = forms.ChatterModelForm
    class Meta: 
        model = models.Chatter
    
admin.site.register(models.Chatter, ChatterModelAdmin)
        