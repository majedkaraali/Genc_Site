from django.db import models
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

# #Two tuple structure
# #The first element in each tuple is the value that will be stored in the database. The second element is displayed by the field’s form widget.
# #Tuple
# PRIORITY = [
# 	('L', 'Low'), #Tuple1
# 	('M', 'Medium'), #Tuple2
# 	('H', 'High'), #Tuple3
# ]

# class Question(models.Model):
# 	title		 			= models.CharField(max_length=60)
# 	question 				= models.TextField(max_length=400)
# 	priority 				= models.CharField(max_length=1, choices=PRIORITY)

# 	def __str__(self):
# 		return self.title


# 	class Meta:
# 		verbose_name = 'The Question'
# 		verbose_name_plural = 'Questions from People'
def upload_location(instance, filename):
	file_path = 'blog/{author_id}/{title}-{filename}'.format(
				author_id=str(instance.author.id),title=str(instance.title), filename=filename)
	return file_path

class Event(models.Model):
    title=           models.CharField(max_length=60)
    location=       models.CharField(max_length=60)
    time=           models.DateTimeField(null=True)
    image		 			= models.ImageField(upload_to=upload_location, null=True, blank=True)
    author 					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Events'
        verbose_name_plural = 'Incoming Events'

@receiver(post_delete, sender=Event)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 

