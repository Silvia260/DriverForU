from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

import uuid

# Create your models here.
class pro_skills(models.Model):
    pro_skills = models.CharField(max_length=100)

    def __str__(self):
        return self.pro_skills

    def save_pro_skills(self):
        self.save()

    @classmethod
    def delete_pro_skills(cls,pro_skills):
        cls.objects.filer(pro_skills=pro_skills).delete()

class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()

class Rate(models.Model):
    rate = models.IntegerField()

    def __str__(self):
        return f"{self.rate}"

    class Meta:
        ordering = ['rate']

    def save_rate(self):
        self.save()

    @classmethod
    def delete_rate(cls,rate):
        cls.objects.filter(rate=rate).delete()


class Driver(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField(default=0)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    pro_skills = models.ManyToManyField(pro_skills)
    rate = models.ForeignKey(Rate,on_delete=models.CASCADE)
    min_hours = models.IntegerField(default=4)
    phonenumber = models.IntegerField()
    featured = models.BooleanField(default=False)
    bio = models.CharField(blank=True, max_length=200)
    image = models.ImageField(upload_to='images/', default='./static/images/img_10_sq')

    def __str__(self):
        return self.first_name

    @classmethod
    def filter_drivers(cls,search_term,skill_search,rate_search):
        drivers = cls.objects.filter(Q(location__location=search_term) & Q(pro_skills__pro_skills__iexact=skill_search) & Q(rate__rate=rate_search))
        return drivers


class Report(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    driver_first_name = models.CharField(max_length=60)
    driver_last_name = models.CharField(max_length=60)
    driver_phonenumber = models.IntegerField()
    driver_rate = models.IntegerField()
    client_id = models.IntegerField()
    client_first_name = models.CharField(max_length=60)
    client_last_name = models.CharField(max_length=60)
    booked_hours = models.IntegerField()
    total_cost = models.IntegerField(default=1600)
    payment_status = models.CharField(max_length=200, default='Completed', editable=False)
    payment_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.transaction_id}"

    @classmethod
    def filter_reports(cls,client_id):
        reports = cls.objects.filter(client_id=client_id)
        return reports


class AllLogin(models.Model):
    user = models.ForeignKey(User)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' ' + str(self.date)
