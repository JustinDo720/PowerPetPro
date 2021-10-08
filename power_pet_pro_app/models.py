from django.db import models
from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import AbstractUser, UserManager
from users.models import CustomUser
from PIL import Image
from django.utils.text import slugify
from django.db.models import Q


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)    # auto generated slug using slugify

    class Meta:
        # With ordering we will be able to see all the categories arranged
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/' # Missing trailing /

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        number = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{number}'    # This way we can have a unique slug for every category
            number += 1
        return unique_slug

    # upon saving the Category
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_image/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='product_image/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # This is going to order our products from the most recent date that the product was added
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        else:
            return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                # Our function make_thumbnail will use pillow etc to resize
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        # We are going to convert to RGB to make sure everything is fine
        img.convert('RGB')
        # then we are going to use Image's thumbnail function given our default size of 300 width x 200 height
        img.thumbnail(size)

        # We are going to use BytesIO to save our image as bytes
        thumb_io = BytesIO()
        img.save(thumb_io, 'png', quality=85)

        # We need to construct a File object ourselves
        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        number = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{number}'
            number += 1
        return unique_slug

    # upon saving the Product
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)


class CartItem(models.Model):
    profile = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # This is going to order our products from the most recent date that the product was added
        ordering = ('-date_added',)

    def __str__(self):
        return self.product.name