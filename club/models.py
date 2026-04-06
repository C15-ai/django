from django.db import models
class Club(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    founded_year = models.IntegerField()
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
