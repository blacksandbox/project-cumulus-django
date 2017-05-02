from __future__ import unicode_literals

from django.urls import reverse
from django.conf import settings
from django.db import models

from .validators import validate_content

# Create your models here.
# Use singular!
class Chatter(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL) # to add default do: default=1 
    content = models.TextField(max_length=150, validators=[validate_content])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.content)
        
    def get_absolute_url(self):
        return reverse("chatter:detail", kwargs={"pk":self.pk})
        
    #happens when you save a model
    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("Cannot be ABC")
            
    #     return super(Chatter, self).clean(*args, **kwargs)