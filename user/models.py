from django.db import models

# Create your models here.
class UserPost(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.CharField(max_length=40)
    postDateTime = models.DateTimeField()

    def __str__(self):
        return self.post