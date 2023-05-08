from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse


class Recipes(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)
    preparation_time = models.IntegerField(help_text="duration in minutes")
    servings = models.IntegerField(help_text="number of servings")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("recipe")
        verbose_name_plural = _("recipes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"pk": self.pk})
        
class Ingredients(models.Model):
    text = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)

    

    class Meta:
        verbose_name = _("ingredient")
        verbose_name_plural = _("ingredients")

    def __str__(self):
        return self.text
        
        
class Instructions(models.Model):
    text = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("instruction")
        verbose_name_plural = _("instructions")

    def __str__(self):
        return self.text
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class CustomUserManager(BaseUserManager):
#     def create_user(self,email,password,first_name, **extra_fields):
#         if not email:
#             raise ValueError("Email field must not be empty!")
#         if not first_name:
#             raise ValueError("First name field must not be empty!")
#         email = self.normalize_email(email)
#         user = self.model(email=email,first_name=first_name, **extra_fields)
#         user.set_password(password)
#         user.save(using=self.db)
#         return user
    
#     def create_superuser(self,email,password,first_name, **extra_fields):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_superuser',True)
        
#         return self.create_user(email,password,first_name, **extra_fields)

# class User(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     last_name = models.CharField(max_length=30,blank=True)
#     first_name = models.CharField(max_length=30,blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     date_joinde = models.DateTimeField(auto_now_add=True)
    
#     objects = CustomUserManager()
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name',]
    
#     def __str__(self):
#         return self.email
    
#     def has_module_perms(self):
#         return self.is_active
#     def has_permission(self,obj=None):
#         return self.is_superuser
#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'
#     def get_short_name(self):
#         return f'{self.first_name}'
    
    


