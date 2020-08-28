from django.db import models
from django.contrib.auth.models import User



class List(models.Model):
      flag_choices = [
          ('1','low importance'),
          ('2','mediocre importance'),
          ('3','very important')
      ]

      user = models.ForeignKey(User,on_delete=models.CASCADE)
      name = models.CharField(max_length=20)
      flag = models.CharField(max_length=10,choices=flag_choices,default='')
      text = models.CharField(max_length=100, default='')
      datetimemade = models.DateTimeField(blank=True)

      def __str__(self):
          return self.name

      class Meta:
          ordering = ['datetimemade']