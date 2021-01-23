from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Course_Registration(models.Model):
    professor = models.CharField(max_length=22,default=None)
    course_name = models.CharField(max_length=25,default=None)
    course_validity = models.IntegerField(default=None)
    fees = models.IntegerField(default=None)
    timing = models.DateTimeField(default=None)
    registered = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)



    def __str__(self):
        return self.course_name

class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course_Registration, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

class InformationModel(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 20)
    address = models.CharField(max_length = 55)
    contact_number = models.IntegerField()
    # coupon_code = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.first_name} , {self.last_name}"



class CouponCode(models.Model):
    coupon = models.CharField(max_length = 45)
    user = models.OneToOneField(User,on_delete = models.CASCADE)

