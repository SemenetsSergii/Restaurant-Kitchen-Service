from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("kitchen:cook-detail", args=[str(self.id)])


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType, on_delete=models.CASCADE, related_name="dishes"
    )
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="dishes"
    )

    class Meta:
        ordering = ["dish_type"]
        verbose_name = "dish"
        verbose_name_plural = "dishes"

    def __str__(self):
        return self.name
