from django.contrib import admin
from .models import Course_Registration,UserModel,InformationModel,CouponCode
# Register your models here.


admin.site.register(Course_Registration)
admin.site.register(UserModel)
admin.site.register(InformationModel)
admin.site.register(CouponCode)