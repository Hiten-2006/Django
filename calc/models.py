from django.db import models
class Customer(models.Model): 
    name=models.CharField(max_length=300, null=True) 
    age=models.CharField(max_length=300, null=True) 
    date=models.DateTimeField(max_length=300, null=True) 
    def __str__(self): 
        return self.name
class Tag(models.Model): 
    name=models.CharField(max_length=300, null=True) 
    def __str__(self): 
        return self.name 
class Product(models.Model): 
    CATEGORY=( 
            ('Indoor','Indoor'), 
            ('Outdoor','Outdoor') 
            ) 
    name=models.CharField(max_length=300,null=True) 
    price=models.FloatField(max_length=300,null=True) 
    category=models.CharField(max_length=300,choices=CATEGORY) 
    tags=models.ManyToManyField(Tag) 
    def __str__(self): 
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
