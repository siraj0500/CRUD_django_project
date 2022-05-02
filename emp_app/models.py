from django.db import models


# Create your models here.

class Employee_reg(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    contact_number = models.IntegerField()
    email = models.EmailField(max_length=50)
    pic = models.ImageField(upload_to='media/', null=True, verbose_name="pic")

    def __str__(self):
        return self.name + ":" + str(self.pic)
