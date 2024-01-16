from django.db import models

# Create your models here.

PRODUCT_TYPES = [
    ('Abonament', 'Subscription'),
    ('Accesoriu', 'Accessory')
]

SHAPE_TYPES = [
    ('Regular', 'Regular'),
    ('Slimfit', 'Slimfit'),
    ('Relaxed Fit', 'Relaxed fit'),
    ('Nu se aplica', 'Not Applicable')
]
class Product(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=PRODUCT_TYPES)
    gender = models.CharField(max_length=1, null=False, default='')
    shape = models.CharField(max_length=100, choices=SHAPE_TYPES)

    def __str__(self):
        return (
            f'Nume:{self.name}, '
            f'Tip:{self.type}, '
            f'Gen:{self.gender}, '
            f'Forma:{self.shape}')
