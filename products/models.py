from django.db import models
import uuid

class Product(models.Model):

    SIZES = {
        "XXS": "XXS",
        "XS": "XS",
        "S": "S",
        "M": "M",
        "L": "L",
        "XL": "XL",
        "XXL": "XXL",
    }

    SIZES = [
        ("XXS", "XXS"), ("XS", "XS"), ("S", "S"),
        ( "M", "M"), ("L", "L"), ("XL", "XL"), ("XXL", "XXL")
    ]

    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField(max_length=800)
    size = models.CharField(max_length=3, choices=SIZES )
    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
