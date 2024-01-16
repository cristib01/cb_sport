from django.contrib.auth.models import User
from django.db import models

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

# Create your models here.
class Sport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=PRODUCT_TYPES)
    gender = models.CharField(max_length=1)
    shape = models.CharField(max_length=100, choices=SHAPE_TYPES)

    def __str__(self):
        return (
            f'Utilizator:{self.user.username}, '
            f'Nume:{self.name}, '
            f'Tip:{self.type}, '
            f'Gen:{self.gender}, '
            f'Forma:{self.shape}')


