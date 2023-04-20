from django.db import models


class Orders(models.Model):
    username = models.CharField(max_length=32)
    send_message = models.CharField(max_length=10000)
    status = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.username} | {self.send_message} | {self.status}"
