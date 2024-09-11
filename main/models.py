from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    # Atribut 
    name = models.CharField(max_length=255)  # Nama
    price = models.IntegerField()            # Harga 
    description = models.TextField()         # Deskripsi

    # Atribut tambahan 
    stock = models.IntegerField(default=0)  # Stok
    category = models.CharField(max_length=100, null=True, blank=True)  # Kategori 
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Gambar item
    
    def __str__(self):
        return self.name

    
