from django.db import models
from Accounts.models import CustomUser


class EyeImage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/') 
    Result = models.CharField(max_length=200, blank=True, null=True) 
    disease = models.CharField(max_length=200, blank=True, null=True)  
    Date = models.DateTimeField(auto_now_add=True) 
    
