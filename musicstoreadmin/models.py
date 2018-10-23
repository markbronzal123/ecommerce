from django.db import models
from django.core.validators import MaxLengthValidator

class Category(models.Model):
    name = models.CharField(max_length = 25)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    sku = models.CharField(unique = True, max_length = 200)
    barcode = models.CharField(max_length = 200)
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length = 500, blank=True, validators=[MaxLengthValidator(500)])
    base_price = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
    product_image = models.ImageField(blank = True, null = True, upload_to = 'product_images/%Y/%m/%D/')
    number_of_stocks = models.IntegerField(default = 0)
    date_created = models.DateField(auto_now_add = True)
    category = models.ManyToManyField(Category, default = None)

    def __str__(self):
        return self.name

    # Displays the image
    def image_tag(self):
        return u'<img src="%s" width="150" height="150" />' % (self.product_image.upload_to)

    image_tag.short_description = 'Image'

class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null = True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name

class Order(models.Model):
    OR = models.CharField(max_length = 15)
    # user fk
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    order_date = models.DateTimeField(auto_now=True)
    raw_total_price = models.DecimalField(max_digits = 6, decimal_places = 2, default = 0)

    def get_cart_items(self):
        return self.products.all()

    def get_cart_total(self):
        return sum([item.product.base_price for item in self.items.all()])

    def __str__(self):
        return self.OR

class UserAccount(models.Model):
    username = models.CharField(max_length = 25)
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 15, null = False)
