from django.db import models
from django.utils import timezone
from accounts.models import UserProfile
class Service(models.Model):
 
  def __unicode__(self):
      return self.name

  serviceType = models.CharField(max_length=3)
  name = models.CharField(max_length=200)
  duration = models.CharField(max_length=200)
  bid = models.FloatField()
  buyOut = models.FloatField()
  starting_date = models.DateTimeField('date published')
  ending_date = models.DateTimeField('expire date')
  user = models.ForeignKey('accounts.UserProfile')
  
  def is_expired(self):
    return self.ending_date <= timezone.now()
  
