from django.db import models

# Create your models here.
class Books(models.Model):
    bookName = models.CharField(max_length=100)
    bookAuthor = models.CharField(max_length=100)
    bookDescription = models.TextField()
    bookTotal = models.IntegerField()
    bookImage = models.ImageField(upload_to='pictures')