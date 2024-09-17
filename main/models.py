from django.db import models
import uuid

# Create your models here.
    
class ItemEntry(models.Model):
    # Atribut
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # ID unik menggunakan UUID
    name = models.CharField(max_length=255)  # Nama item 
    category = models.CharField(max_length=100, null=True, blank=True)  # Kategori
    size = models.CharField(max_length=50, null=True, blank=True) 
    color = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)  # Harga
    # image = models.ImageField(upload_to='images/', null=True, blank=True)  # Gambar item
    
   

    
