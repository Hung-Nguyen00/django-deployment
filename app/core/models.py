from django.db import models

# Create your models here.
class Sample(models.Model):
    attachment = models.FileField()
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.title