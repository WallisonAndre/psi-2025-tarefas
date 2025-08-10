from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)  # False para pendente, True para concluída
    deadline = models.DateField()

    def __str__(self):
        return self.name