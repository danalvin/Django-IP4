from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class nieghbor(models.Model):
    name = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hoodadmin", null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save_hood(self):
        self.save()

    @classmethod
    def find_neighbor_hood(cls, hood_id):
        hood = cls.objects.filter(id=hood_id)
        return hood


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    identity = models.CharField(max_length=100, null=True, blank=True)
    profilepicture = models.ImageField(upload_to='images/', blank=True)
    neighbor_hood = models.ForeignKey(nieghbor, on_delete=models.CASCADE, related_name="hood", null=True,
                                      blank=True)
    secondary_email = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user']

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Business(models.Model):
    name = models.CharField(max_length=100, null=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="business", null  =True, default='')
    neighbor_hood = models.ForeignKey(nieghbor, on_delete=models.CASCADE, related_name="hoodbus", null=True, default='')
    email = models.CharField(max_length=100, null=True, default='example@mail.com')


    class Meta:
        ordering = ['name']

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        business = cls.objects.filter(id=business_id)
        return business

    @classmethod
    def search_by_title(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business


class Post(models.Model):
    post = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="adminpost", null=True, blank=True)
    neighbor_hood = models.ForeignKey(nieghbor, on_delete=models.CASCADE, related_name="hoodpost", null=True,
                                      blank=True)


class Comments(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user')
    comments = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
