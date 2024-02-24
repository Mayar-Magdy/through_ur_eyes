from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from datetime import datetime


keys = ["Cairo", "Alexandria", "Port Said", "Suez", "Damietta", "Daqahliya", "Sharqiya", "Qulioubiya", "Kafr El-Sheikh", "Gharbiya", "Monofiya", "Beheira", "Ismailia", "Bani Suef", "Fayyoum", "Minya", "Assiut", "Sohag", "Qena", "Aswan", "Luxor", "Red Sea", "New Valley", "Marsa Matrouh", "North Sinai", "South Sinai", "Giza","Outside the Republic"]
values = [1, 2, 3, 4, 11, 12, 13, 14, 15,16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35,21,88]
my_map = dict(zip(keys, values))


CITY_CHOICES = [
        ('Alexandria', 'Alexandria'),
        ('Assiut', 'Assiut'),
        ('Aswan', 'Aswan'),
        ('Beheira', 'Beheira'),
        ('Bani Suef', 'Bani Suef'),
        ('Cairo', 'Cairo'),
        ('Daqahliya', 'Daqahliya'),
        ('Damietta', 'Damietta'),
        ('Fayyoum', 'Fayyoum'),
        ('Gharbiya', 'Gharbiya'),
        ('Giza', 'Giza'),
        ('Ismailia', 'Ismailia'),
        ('Kafr El-Sheikh', 'Kafr El-Sheikh'),
        ('Luxor', 'Luxor'),
        ('Marsa Matrouh', 'Marsa Matrouh'),
        ('Minya', 'Minya'),
        ('Monofiya', 'Monofiya'),
        ('New Valley', 'New Valley'),
        ('North Sinai', 'North Sinai'),
        ('South Sinai', 'South Sinai'),
        ('Port Said', 'Port Said'),
        ('Qulioubiya', 'Qulioubiya'),
        ('Qena', 'Qena'),
        ('Red Sea', 'Red Sea'),
        ('Sharqiya', 'Sharqiya'),
        ('Sohag', 'Sohag'),
        ('Suez', 'Suez'),
        ('Outside the Republic','Outside the Republic'),
    ]
def validate_national_id_and_dob(value):
    
    flag=True
    national_number, date_of_birth , city , gender= value #tuple
    date_of_birth = str(date_of_birth)
    date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()

    #1 16 61 11 1111117
    #2023-06-27
    century = int(national_number[0])
    year = int(national_number[1:3])
    month = int(national_number[3:5])
    day = int(national_number[5:7])
    if century == 2:
        year += 1900
    elif century == 3:
        year += 2000
    if year != date_of_birth.year or month != date_of_birth.month or day != date_of_birth.day:
        flag=False
    if my_map[city] != int(national_number[7:9]):
        flag=False
    if gender == 'Female' and int(national_number[12])%2 != 0 :
        flag=False
    elif gender == 'Male'and int(national_number[12])%2 == 0 :
        flag=False
    if not flag :
     raise ValidationError("The national number and the date of birth do not match")



    
    
    

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Please enter your email address"))

        email = self.normalize_email(email)
        # date_of_birth = extra_fields.pop('date_of_birth', None)

        new_user = self.model(email=email, **extra_fields)
        new_user.set_password(password)

        new_user.save(using=self._db)
        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Super user should have is_staff True'))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Super user should have is_superuser True'))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Super user should have is_active True'))

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = models.CharField(max_length=200)
<<<<<<< HEAD
    national_number = models.CharField(max_length=14, unique=True, blank=True,validators=[validate_national_id_and_dob])
=======
    national_number = models.CharField(max_length=14, unique=True, blank=True)
>>>>>>> 054841a07e7dee4fc756d8b9d27b65421b79ab72
    phone_number = models.TextField(null=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=100 ,choices=CITY_CHOICES, default='Cairo')
    USERNAME_FIELD = 'national_number'
    REQUIRED_FIELDS = ['username', 'email']
    objects = CustomUserManager()
    def __str__(self):
        return self.username
    def save(self, *args, **kwargs):
        # You can write your own logic here
        if self.national_number and self.date_of_birth and self.city and self.gender:
            try:
                validate_national_id_and_dob((self.national_number, self.date_of_birth, self.city, self.gender))
            except ValidationError as e:
                raise ValidationError({'national_number': e.message})
        # Don't forget to call the super method
        super().save(*args, **kwargs)
    
 