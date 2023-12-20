from django.db import models

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')
    likes = models.IntegerField(default=0)
    description = models.TextField()

class Testimonial(models.Model):
    name = models.TextField()
    description = models.TextField()
    profile_pic = models.ImageField(upload_to='testimonial_images/')

class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()
    description = models.TextField()
