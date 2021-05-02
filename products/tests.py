from django.test import TestCase
from products.models import Brand, Product

data_brand = {'name':'Marca X'}
data_product = {'sku': '1', 'name':'Producto X', 'price': 10}


class BrandModelTest(TestCase):
    def test_create_brand(self):
        brand, brand_created = Brand.objects.get_or_create(**data_brand)
        self.assertEquals(brand.name, 'Marca X')


class ProductModelTest(TestCase):
    def test_create_product(self):
        brand, brand_created = Brand.objects.get_or_create(**data_brand)
        product, product_created = Product.objects.get_or_create(**data_product, brand=brand)
        self.assertEquals(product.name, 'Producto X')