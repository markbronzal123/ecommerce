from django.test import TestCase

from .models import Product

class ProductModelTests(TestCase):
    def test_is_sku_unique(self):
        _sku = '0939029124124'
        prod_skus = Product.list_filter(sku = '0939029124124')
        self.assertEqual(_sku, prod_skus)
