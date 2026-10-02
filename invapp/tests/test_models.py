from django.test import TestCase
from django.contrib.auth.models import User
from invapp.models import Product, Profile


class ModelsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="usertest", password="passwordtest")


    def test_product_model(self):
        product = Product.objects.create(
            user = self.user,
            name  = "Computer",
            sku = "C03",
            price  = 1200,
            quantity = 43,
            supplier = "Dell",
            category = "computers"
        )

        self.assertEqual(product.name, "Computer")
        self.assertEqual(product.sku, "C03")
        self.assertEqual(product.price, 1200)
        self.assertEqual(product.quantity, 43)
        self.assertEqual(product.supplier, "Dell")
        self.assertEqual(product.category, "computers")


    def test_profile_model(self):
        profile = Profile.objects.create(
            user = self.user,
            phone_number = "0702341629"
        )

        self.assertEqual(profile.phone_number, "0772341629")