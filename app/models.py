from django.db import models
from datetime import datetime
from baby.models import Baby

class BabyTrack(models.Model):
    name = models.ForeignKey(Baby, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=datetime.now(), blank=False)
    wet = models.BooleanField()
    dirty = models.BooleanField()
    leftside = models.IntegerField(default=0)
    rightside = models.IntegerField(default=0)
    sup_amount = models.DecimalField(max_digits=3, decimal_places=1)
    sup_f = models.BooleanField()
    sup_b = models.BooleanField()
    
   


