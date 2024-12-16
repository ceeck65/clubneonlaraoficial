from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_countries.fields import CountryField

# Create your models here.

# MODEL PROFILE

class Profile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	image = models.ImageField(default='users/user_profile.jpg', upload_to='users/')
	birthday = models.DateField(max_length=80, null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	country = CountryField()
	gender = models.CharField(max_length=80, null=True, blank=True)
	job = models.CharField(max_length=80, null=True, blank=True)
	telephone = models.CharField(max_length=80, null=True, blank=True)
	biography = models.TextField(max_length=400, null=True, blank=True)


	class Meta:
		verbose_name = 'Perfil'
		verbose_name_plural = 'Perfiles'
		ordering = ['-id']

	def __str__(self):
		return '{}'.format(self.user)


def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)