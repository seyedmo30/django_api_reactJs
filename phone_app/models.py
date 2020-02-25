<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

class Grp(models.Model):
    name=models.CharField(max_length=30)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contacts', args=[self.id])



class Phone(models.Model):


    name=models.CharField(max_length=30)
    number=models.IntegerField(12)
    group=models.ForeignKey(Grp,null='true' ,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    document = models.ImageField(upload_to='documents/' )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('update', args=[self.id])
=======
from django.db import models
from django.contrib.auth.models import User


class Grp(models.Model):
    name=models.CharField(max_length=30)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Phone(models.Model):


    name=models.CharField(max_length=30)
    number=models.IntegerField(12)
    group=models.ForeignKey(Grp,null='true' ,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
>>>>>>> 2a6c62489d1acf598d77c6946474d1a50c5119bc
