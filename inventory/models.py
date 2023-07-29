from django.db import models

class SparePart(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
