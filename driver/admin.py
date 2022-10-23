from django.contrib import admin
from .models import pro_skills, Driver, Location, Rate, Report

# Register your models here.
admin.site.register(pro_skills)
admin.site.register(Location)
admin.site.register(Driver)
admin.site.register(Rate)
admin.site.register(Report)
