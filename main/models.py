from django.db import models

# Create your models here.
class SyreEntry(models.Model):
    mood = models.CharField(max_length=255) #product
    time = models.DateField(auto_now_add=True) #price
    feelings = models.TextField() #desc
    mood_intensity = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5
