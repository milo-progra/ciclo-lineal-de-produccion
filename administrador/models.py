from django.db import models

# Create your models here.
class LogTelegram(models.Model):
    id_telegram = models.CharField(max_length=100)
    timesstap = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
