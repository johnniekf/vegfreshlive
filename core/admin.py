from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {}


@admin.register(RecipeSet)
class SetAdmin(admin.ModelAdmin):
    prepopulated_fields = {}


@admin.register(Core)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(FoodGroup)
class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {}


@admin.register(Ingredient)
class ingredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {}
