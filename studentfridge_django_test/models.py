import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

# Create your models here.

#Changes to default user authentication model here.
class FridgeUsers(AbstractUser):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)


class Ingredients (models.Model):
    id = models.UUIDField(Primary_key = True, defualt = uuid.uuid4, editable = False)
    name = models.CharField(max_length = 50, unique = True) #We can only have one ingredient of a specific type. For instance: White Onion is an ingredient
    description = models.CharField(max_length = 500, blank = True, null = True) # this field is optional.
    date_added = models.DateTimeField(default = now())    
    date_updated = models.DateTimeField(null = True, blank = True)
    #is_raw = models.BooleanField (default = True) #Raw ingredients cannot be part of a non raw ingredient.
    
class Products (models.Model):
    id = models.UUIDField(Primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length= 50)
    description = models.CharField(max_length= 50)
    sku = models.IntegerField(null = True, blank = True) # Or barcode number, or whatever. 
    date_added = models.DateTimeField(default = now())    
    date_updated = models.DateTimeField(null = True, blank = True)
    
class ProductIngredients(models.Model):
    id = models.UUIDField(Primary_key = True, default = uuid.uuid4, editable = False)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredients)
    date_added = models.DateTimeField(default =now())
    date_updated = models.DateTimeField(null = True)
    
class Diet(models.Model):
    id = models.UUIDField(Primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length = 50)
    created_by= models.ForeignKey(FridgeUsers)
    is_private = models.BooleanField(Default = True)