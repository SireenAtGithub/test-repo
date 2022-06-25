from django.db import models


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    score = models.IntegerField()

    def __str__(self):
        return self.id + " " + self.name + " " + self.score
