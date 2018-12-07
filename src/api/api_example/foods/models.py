from django.db import models


class Foods(models.Model):
    foodname = models.CharField(max_length=120, null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)
    protein = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.foodname)
