from django.db import models
from django.utils import timezone

class User(models.Model):
  
  def __unicode__(self):
      return self.name

  name = models.CharField(max_length=200)
  feedback = models.FloatField()

class Service(models.Model):
 
  def __unicode__(self):
      return self.name
  serviceType = models.IntegerField()
  name = models.CharField(max_length=200)
  duration = models.CharField(max_length=200)
  bid = models.FloatField()
  buyOut = models.FloatField()
  starting_date = models.DateTimeField('date published')
  ending_date = models.DateTimeField('expire date')
  user = models.ForeignKey(User)
  
  def is_expired(self):
    return self.ending_date <= timezone.now()
  
