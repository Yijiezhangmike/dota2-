from django.db import models

# Create your models here.dd
class User(models.Model):
	"""docstring for user"""
	user_name = models.CharField(max_length=200)
	user_email = models.CharField(max_length=200)
	user_password = models.CharField(max_length=200)

	def __str__(self):
		return f"{self.user_name} {self.user_email}"

