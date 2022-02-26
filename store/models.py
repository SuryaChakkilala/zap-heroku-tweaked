from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    image = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    description = models.TextField(default='desc')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url

class Order(models.Model):
    user = models.TextField(default='_')
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    product_name = models.TextField(default='_')

    def __str__(self):
        return str(self.id)