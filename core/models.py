from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class Ingredient(models.Model):
    IngName = models.CharField(max_length=30)
    IngType = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.IngName


class Core(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(null=True)
    category = models.CharField(max_length=10)
    cookTime = models.CharField(max_length=20)
    prepTime = models.CharField(max_length=20)
    ingredients = models.ManyToManyField(Ingredient)
    process = models.TextField(null=True)
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(default='default.png', blank=True)

    def get_absolute_url(self):
        return reverse('core:single', args=[self.slug])

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title


class FoodGroup(models.Model):
    group_name = models.CharField(max_length=200)
    recipe = models.ManyToManyField(Core)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('core:single', args=[self.slug])

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.group_name


class RecipeSet(models.Model):
    set_name = models.CharField(max_length=200)
    recipe = models.ManyToManyField(Core)
    published = models.DateField(default=timezone.now)

    def __str__(self):
        return self.set_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)