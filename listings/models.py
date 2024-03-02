from django.db import models
from django.utils.timezone import now
from realtors.models import Realtor
from useraccount.models import UserAccount

class Listing(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'

    class HouseType(models.TextChoices):
        RESIDENTIAL = 'Residential'
        COMMERCIAL = 'Commercial'    
    
    class Furnishing(models.TextChoices):
        FURNISH = 'Furnished'
        SEMIFURNISH = 'Semifurnished'
        UNFURNISH = 'Unfurnished'

    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='listings')
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    society = models.TextField()
    sale_type = models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE)
    house_type = models.CharField(max_length=50, choices=HouseType.choices, default=HouseType.RESIDENTIAL)
    price = models.DecimalField(max_digits=100, decimal_places=5)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    balcony = models.IntegerField() 
    furnish_type = models.CharField(max_length=50, choices=Furnishing.choices, default=Furnishing.FURNISH)
    carpet_area = models.IntegerField()
    floor_no = models.CharField(max_length=20)
    facing = models.CharField(max_length=20)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title
