from django.db import models
from django.utils import timezone
 
# Create your models here.
class TodoListItem(models.Model):
    content = models.TextField() 
    date=models.DateField(auto_now_add=True)
    user=models.CharField(max_length=100)
    
# Create your models here.