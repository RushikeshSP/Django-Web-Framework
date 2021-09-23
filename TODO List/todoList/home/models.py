from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=30)
    date = models.DateField()
    desc = models.TextField()

    def __str__(self):
        return self.task_name + "  On Date:  " + str(self.date)