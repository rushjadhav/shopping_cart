from django.db import models

from django.contrib.auth.models import User
# Create your models here.

status_choices = (('A', 'Active'), ('I', 'Inactive'))

class Category(models.Model):
    
    name = models.CharField(verbose_name='Name', max_length=80, null=False, blank=False, unique=True)

    description = models.TextField(verbose_name='Description', null=True, blank=True)

    status = models.CharField(verbose_name='Status', choices=status_choices, max_length=1, default='A',
                              help_text='Only active categories are shown on site.')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):

    name = models.CharField(verbose_name='Name', max_length=80, null=False, blank=False)

    category = models.ForeignKey(Category, related_name='products')

    price = models.DecimalField(verbose_name='Price', null=False, blank=False, max_digits=10, decimal_places=5)

    description = models.TextField(verbose_name='Description', null=True, blank=True)

    image = models.ImageField(null=True, blank=True)

    status = models.CharField(verbose_name='Status', choices=status_choices, max_length=1, default='A')

    def __unicode__(self):
        return "%s(%s)" %(self.name, self.category)

    class Meta:
        unique_together = (('name', 'category'))

class Order(models.Model):

    order_choices = (('C', 'Completed'),('N', 'Not Completed'))

    user = models.ForeignKey(User, related_name='orders')

    shipping_address = models.TextField(verbose_name='Shipping Address')

    order_date = models.DateField(verbose_name='Order Date', auto_now_add=True)

    delivery_date = models.DateField(verbose_name='Delivered on', null=True, blank=True)

    status = models.CharField(max_length=1, choices=order_choices, default='N')

    products = models.ManyToManyField(Product, through='ProductOrderMap')

    def __unicode__(self):
        return "%s(%s)" %(self.user, self.id)

class ProductOrderMap(models.Model):

    product = models.ForeignKey(Product)

    order = models.ForeignKey(Order)

    quantity = models.IntegerField(null=False, blank=False)

    class Meta:
        verbose_name_plural = "Products"

    def __unicode__(self):
        return self.product.name

