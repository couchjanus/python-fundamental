from django.db import models

# Create your models here.

class Category(models.Model):
    """
    Model representing a product category (e.g. Car, Computer).
    """
    name = models.CharField(max_length=200, help_text="Enter a product category (e.g. Car, Computer etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
