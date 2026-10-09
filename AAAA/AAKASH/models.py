from django.db import models
from django.contrib import admin
class User(models.Model):
    Mobilenumber=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=15)
    Address=models.TextField()
    Productdetails=models.TextField()
    offer_code=models.CharField()
class UserAdmin(admin.ModelAdmin):
    list_display=["Mobilenumber","Name","Address","Productdetails","offer_code",]
