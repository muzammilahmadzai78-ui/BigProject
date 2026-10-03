from django.test import TestCase
from invapp.models import Product, Profile
from django.contrib.auth.models import User

class ModelsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(password="testpassword", username="testuser")


    def test_product_model(self):
        product = Product.objects.create(
            user = self.user,
            sku = "C04",
            name = "Computer",
            price = 320,
            quantity = 30,
            supplier = "dell",
            category = "computers"
        )

        self.assertEqual(product.name, "Computer")
        self.assertEqual(product.sku, "C04")
        self.assertEqual(product.price, 320)
        self.assertEqual(product.quantity, 30)
        self.assertEqual(product.supplier, "dell")
        self.assertEqual(product.category, "computers")
        self.assertEqual(str(product), "Computer")

    def test_user_model(self):
        user = User.objects.create_user(
            username = "usertest",
            password = "testpassword",
            first_name =  "Muzammil",
            last_name  = "Ahmadzai",
            email =  "muzammilahmadzai78@gmail.com"
        )

        self.assertEqual(user.username, "usertest")
        self.assertTrue(user.check_password('testpassword'))
        self.assertEqual(user.first_name, "Muzammil")
        self.assertEqual(user.last_name, "Ahmadzai")
        self.assertEqual(user.email, "muzammilahmadzai78@gmail.com")

    def test_profile_model(self):
        profile = Profile.objects.create(
            user = self.user,
            phone_number = "0728108323"
        )

        self.assertEqual(profile.phone_number, "0728108323")