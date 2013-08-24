from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaLanguageBaseProfile

class UserProfile(UserenaLanguageBaseProfile):
  user = models.OneToOneField(User,unique=True,verbose_name=_('user'),related_name='my_profile')
  feedback = models.CharField(_('feedback'),max_length=5)
