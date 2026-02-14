from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField(help_text="List ingredients, separated by commas")
    steps = models.TextField(help_text="Step-by-step instructions")
    prep_time = models.IntegerField(default=0, help_text="Preparation time in minutes")
    cook_time = models.IntegerField(default=0, help_text="Cooking time in minutes")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)

    def __str__(self):
        return self.title
