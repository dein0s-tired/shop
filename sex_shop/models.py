from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.PositiveIntegerField(default=0)  # todo think about it
    category = models.ForeignKey(Category)
    manufacturer = models.ForeignKey(Manufacturer)
    available_count = models.PositiveIntegerField(default=0)  # todo think about it

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class News(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    publish_date = models.DateTimeField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
