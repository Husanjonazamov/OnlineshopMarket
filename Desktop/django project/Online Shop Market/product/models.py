from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to="rasm/")
    character = models.TextField()
    UZ = "so'm"
    RU = "P"
    ENG = "$"
    the_price = (
        (UZ, "so'm"),
        (RU, "P"),
        (ENG, "$")
    )
    price_type = models.CharField(max_length=10, 
                                  choices=the_price,
                                  default="so'm")
    price = models.IntegerField()

    
    def __str__(self):
        return self.name

    
    def save(self, *args, **kwargs ):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Sneakers(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    character = models.TextField()
    UZ = "so'm"
    RU = "P"
    ENG = "$"
    the_price = (
        (UZ, "so'm"),
        (RU, "P"),
        (ENG, "$")
    )
    price_type = models.CharField(max_length=10, 
                                  choices=the_price,
                                  default="so'm")
    price = models.IntegerField()
    image = models.ImageField(upload_to="post/")

    def __str__(self) -> str:
        return self.name

class Buy(models.Model):
    name = models.CharField(max_length=156)
    phone = models.CharField(max_length=30)
    product = models.ForeignKey(Sneakers, on_delete=models.CASCADE, null=True)
    ALL_SIZES = (
        ("36","36"),
        ("37","37"),
        ("38","38"),
        ("39","39"),
        ("40","40"),
        ("41","41"),
        ("42","42"),
        ("43","43"),
        ("44","44"),
    )
    size = models.CharField(max_length=100, choices=ALL_SIZES)
    ALL_VALUES = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    )
    how = models.CharField(max_length=100, choices=ALL_VALUES)
    map = models.TextField()
    email = models.EmailField(blank=True)

    def __str__(self) -> str:
        return self.name

class Advertising(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    image = models.ImageField(upload_to="anons/")

    def __str__(self) -> str:
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=112)
    image = models.ImageField("image/")

    def __str__(self) -> str:
        return self.title

class Feel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField("feel/")


    def __str__(self) -> str:
        return self.title
# Create your models here.
