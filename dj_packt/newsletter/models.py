from django.db import models

class NewsItem(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    body = models.TextField()

    def __str__(self):
        return self.title

