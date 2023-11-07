from django.db import models

# Create your models here.
class College_store(models.Model):
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    age=models.TextField()
    dob=models.CharField(max_length=250)
    gender=models.TextField()
    phone=models.TextField()
    mailid=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    dept=models.CharField(max_length=250)
    course=models.CharField(max_length=250)
    puropose=models.TextField()
    mat_provd=models.TextField()
class User_reg(models.Model):
    username=models.CharField(max_length=65)
    password=models.CharField(max_length=65)
    c_password=models.CharField(max_length=65)



    def __str__(self):
        return self.firstname
    def __str__(self):
        return self.username