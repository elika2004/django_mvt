from django.db import models
from django.contrib.auth.models import User





class Ability(models.Model):
    name=models.CharField( max_length=200)
    def __str__(self):
        return self.name

class Agent(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ability=models.ForeignKey(Ability,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='agent',default="defult.jpg")
    twiter=models.CharField( max_length=100)
    facebook=models.CharField( max_length=100)
    insagram=models.CharField( max_length=100)
    linkedin=models.CharField( max_length=100)
    state=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name