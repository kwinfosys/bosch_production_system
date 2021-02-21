from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = ((1,'Adminuser'),(2,'Superuser'),(3,'Expertuser'),(4,'Normaluser'))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=12)
    employee_number = models.CharField(max_length=10)

class Department(models.Model):
    main_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=8)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.name

class Adminuser(models.Model):
    main_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to="bosch_production_app/uploaded_profile_pics")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    

class Superuser(models.Model):
    main_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to="bosch_production_app/uploaded_profile_pics")
    grade = models.CharField(max_length=5)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    

class Expertuser(models.Model):
    main_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to="bosch_production_app/uploaded_profile_pics")
    grade = models.CharField(max_length=5)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    

class Normaluser(models.Model):
    main_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to="bosch_production_app/uploaded_profile_pics")
    grade = models.CharField(max_length=5)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Adminuser.objects.create(user=instance, mobile_number="")
        if instance.user_type == 2:
            Superuser.objects.create(user=instance, mobile_number="", grade="", department=Department.objects.get(main_id=1))
        if instance.user_type == 3:
            Expertuser.objects.create(user=instance, mobile_number="", grade="", department=Department.objects.get(main_id=1))
        if instance.user_type == 4:
            Normaluser.objects.create(user=instance, mobile_number="", grade="", department=Department.objects.get(main_id=1))

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminuser.save()
    if instance.user_type == 2:
        instance.superuser.save()
    if instance.user_type == 3:
        instance.expertuser.save()
    if instance.user_type == 4:
        instance.normaluser.save()
