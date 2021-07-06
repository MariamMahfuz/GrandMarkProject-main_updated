from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class appointment(models.Model):

    GENDER_CHOICES = [
        ('gender', 'Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]

    BLOOD_GROUP_CHOICES = [
        ('blood', 'Blood Group'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB-'),
        ('AB-', 'AB-')
    ]


    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Patient')
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    user_mail=models.EmailField()
    dob=models.DateTimeField(auto_now_add=False, null=True)
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES, default='gender')
    blood_group = models.CharField(max_length=15, choices=BLOOD_GROUP_CHOICES, blank=True, default='blood')
    phone = models.IntegerField(max_length=20)
    address_1 = models.TextField(max_length=300)
    problem = models.CharField(max_length=300)
    city = models.CharField(max_length=40)
    state=models.CharField(max_length=20, null=False)
    zipcode = models.IntegerField(max_length=10)
    avatar = models.ImageField(upload_to='appointment_candidate_pics', blank=True, null=True)

    def __str__(self):
        return self.first_name




