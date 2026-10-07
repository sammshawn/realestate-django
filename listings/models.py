from django.db import models


class Property(models.Model):
    """A real estate property listing."""

    PROPERTY_TYPES = [
        ("house", "House"),
        ("apartment", "Apartment"),
        ("land", "Land"),
        ("commercial", "Commercial"),
    ]

    STATUS_CHOICES = [
        ("available", "Available"),
        ("sold", "Sold"),
        ("rented", "Rented"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)

    location = models.CharField(max_length=200)
    city = models.CharField(max_length=100, default="Nairobi")

    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES, default="house")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available")
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    area_sqft = models.PositiveIntegerField(default=0, help_text="Area in square feet")

    image = models.ImageField(upload_to="properties/", blank=True, null=True)

    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.title

    def formatted_price(self):
        return f"KES {self.price:,.0f}"