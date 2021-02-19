from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CustomUser)
admin.site.register(models.Department)
admin.site.register(models.Adminuser)
admin.site.register(models.Expertuser)
admin.site.register(models.Normaluser)