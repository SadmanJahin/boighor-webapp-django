from django.db import models
from django.db import connection


# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    bookName = models.CharField(max_length=30 )
    bookWriter = models.CharField(max_length=40)
    release_date = models.DateField()
    price = models.IntegerField()
    bookCategory = models.CharField(max_length=50)
    bookImage= models.ImageField(upload_to='book/images/',blank='false')

    def __str__(self):
        return self.bookName

    def Truncate(cls):
        cursor = connection.cursor()
        cursor.execute("TRUNCATE TABLE index_Person RESTART IDENTITY")
    def getUserName(self,userId):
        cursor = connection.cursor()
        cursor.execute("SELECT username FROM authentication_account where id="+str(userId))
        data = cursor.fetchall()
        return data

