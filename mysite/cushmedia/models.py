from django.db import models

# Create your models here.

portfolio_category =(
    ('outdoor', 'outdoor'),
    ('weddings', 'weddings'),
    ('portraits', 'portraits'),
    ('engagement', 'engagement'),
    ('couples', 'couples'),
    ('others', 'others')
)

class Portfolio(models.Model):
    category = models.CharField(max_length=20, choices= portfolio_category, default='outdoor')
    img = models.ImageField(upload_to='pics')



class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    #occupation = models.TextField()
   # img = models.ImageField(upload_to='pics')
    testimony = models.TextField()

class Services(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()

