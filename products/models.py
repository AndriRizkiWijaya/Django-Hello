from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.
CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('H', 'Hoddie'),
    ('C', 'Cap'),
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

class Item(models.Model):
    title           = models.CharField(max_length=100)
    slug            = models.SlugField(max_length=100, unique=True, db_index=True)
    price           = models.FloatField()
    price_discount  = models.FloatField(blank=True, null=True)
    label           = models.CharField(choices=LABEL_CHOICES, max_length=2)
    category        = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    description     = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Products:detail_view", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("Products:add_to_cart_view", kwargs={"slug": self.slug})

    def get_remove_from_cart_url(self):
        return reverse("Products:remove_from_cart_view", kwargs={"slug": self.slug})


class OrderItem(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item        = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=1)
    ordered     = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items           = models.ManyToManyField(OrderItem)
    start_date      = models.DateTimeField(auto_now_add=True)
    ordered_date    = models.DateTimeField()
    ordered         = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
