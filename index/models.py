from django.db import models
from django.db import connection
# Create your models here.

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)
    messege = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def Truncate(cls):
        cursor = connection.cursor()
        cursor.execute("TRUNCATE TABLE index_Person RESTART IDENTITY")
    
class Footer(models.Model):
    id = models.AutoField(primary_key=True)
    footer_image1 = models.ImageField(upload_to='index/images/footer/', blank='false')
    footer_image2 = models.ImageField(upload_to='index/images/footer/', blank='false')
    footer_contactus_address=models.CharField(max_length=50)
    footer_contactus_phone = models.CharField(max_length=50)
    footer_contactus_email = models.CharField(max_length=50)
    
        
    
    def __str__(self):
        return "Footer "+str(self.id)
    
    def Truncate(cls):
        cursor = connection.cursor()
        cursor.execute("TRUNCATE TABLE index_Footer RESTART IDENTITY")
         
    