from django.db import models
import datetime

class Event(models.Model):
    theme_id = models.IntegerField(default=1)  # Ensure theme_id is set for all events
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(default=datetime.date.today)
    media_type = models.CharField(max_length=10, choices=[('photo', 'Photo'), ('audio', 'Audio'), ('video', 'Video')], default='photo')
    media_file = models.FileField(upload_to='media/', default='media/placeholder.JPG')
