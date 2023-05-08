from django.contrib import admin
from .models import Recipes,Instructions,Ingredients

class IngredientsInline(admin.TabularInline):
    model = Ingredients
    
class InstructionsInline(admin.TabularInline):
    model = Instructions

class RecipesAdmin(admin.ModelAdmin):
    inlines = [IngredientsInline,InstructionsInline]
    
# Register your models here.
admin.site.register(Recipes,RecipesAdmin)
admin.site.register(Ingredients)
admin.site.register(Instructions)
