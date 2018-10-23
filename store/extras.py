import random
import string
from datetime import date
import datetime

from musicstoreadmin.models import OrderItem

def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str

def get_item_count():
    count = OrderItem.objects.all().count()
    return count

def cart_total_price():
    items = OrderItem.objects.all()
    total_price = 0
    for item in items:
        total_price += item.product.base_price
    return total_price
