from django.db import models

class web(models.Model):
    web_name=models.CharField(max_length=100)
    web_description=models.TextField()
   