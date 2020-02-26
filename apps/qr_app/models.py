from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models

# Create your models here.
class Master(models.Model):
    first_name = 'Leo'
    last_name = 'Kevin'
    email = 'email@email.com'
    password = 'email'

class UserManager(models.Manager):
    def validator(self, postData):
        errors={}
        if len(postData['first_name']) < 2:
            errors['first_name']='first name must have 2 characters minimum'
        if len(postData['last_name']) < 2:
            errors['last_name']='last name must have 2 characters minimum'
        try:
            validate_email(postData['email']) 
        except ValidationError as e:
            errors['email']='invalid email'
        if len(postData['password']) < 8:
            errors['password']='password must be 8 characters minimum'
        if postData['password']!=postData['confirm_password']:
            errors['match']='passwords do not match'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
    #user.qrs_validated.all() will give yo ua list of all this users objects
    def __repr__ (self):
        return str(self.__dict__)
    
class All_QR(models.Model):
    all_codes={}
    #name 
    #contact 
    #other company details
    #company.qr_codes.all() will give you all this companies qrcode objects 

class QR(models.Model):
    text = models.TextField()
    # qr_image = models.ImageField(null=True, blank=True)
    imgfile = models.ImageField(upload_to='qr_img/', blank=True, null=True)
    validated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="qrs_validated", null=True, blank=True)
    
    def __repr__ (self):
        return str(self.__dict__)
    
    