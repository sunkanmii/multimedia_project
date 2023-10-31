from django.db import models

# Create your models here.
class MediaFiles(models.Model):
    img_link = models.URLField(max_length = 200)
    