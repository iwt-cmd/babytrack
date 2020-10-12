from django.db import models

class Baby(models.Model):
    name = models.CharField(max_length=15)
    image = models.ImageField(upload_to='photos')
    def __str__(self):
        return self.name