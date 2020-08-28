from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(max_length=200 , blank=True, default='')

    def __str__(self):
        return self.bio[1:5]

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Blogpost(models.Model):
    Choices = (
        ('science','science'),
        ('Food','Food'),
        ('Entertainment','Entertainment'),
        ('Music','Music'),
        ('Travel','Travel'),
        ('Astrology','Astrology'),
        ('Other','Other')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=2000 )
    like = models.ManyToManyField(User, related_name = 'likes')
    dislike = models.ManyToManyField(User, related_name = 'dislikes')
    category = models.CharField(max_length=15,choices=Choices)
    heading = models.CharField(max_length=100)
    subheading = models.TextField(max_length=100 , null=False)

    def likes_count(self):
        return self.like.count()

    def dislikes_count(self):
        return self.dislike.count()

    def __str__(self):
        return  self.heading
