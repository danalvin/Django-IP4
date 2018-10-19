from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class nieghbor(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hoodadmin", null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    ID = models.CharField(max_length=100, null=True, blank=True)
    profilepicture = models.ImageField(upload_to='images/', blank=True, default="/black.png")
    neighbor_hood = models.ForeignKey(nieghbor, on_delete=models.CASCADE, related_name="hood", null=True,
                                      blank=True)
    secondary_email = models.CharField(max_length=100, null=True, blank=True)



