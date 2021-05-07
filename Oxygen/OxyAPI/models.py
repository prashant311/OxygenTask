from django.db import models


class OxygenModel(models.Model):
    address = models.CharField(max_length=200)
    businessName = models.CharField(max_length=100)
    personName = models.CharField(max_length=20, blank=True)
    contact = models.IntegerField(max_length=10)
    verifiedStatus = models.BooleanField()
    timeStamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['verifiedStatus', 'timeStamp']
