from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name