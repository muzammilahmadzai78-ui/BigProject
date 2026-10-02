from django.test import TestCase
from invapp.forms import ProfileForm, ProductForm, RegisterForm


class TestForms(TestCase):
    def test_product_form_data(self):
        form = ProductForm(data={
            "name": "Computer",
            "sku": "C03",
            "price": 30,
            "quantity": 3,
            "supplier": "Dell",
            "category": "computers"
        })

        self.assertTrue(form.is_valid())


    def test_product_form_no_data(self):
        form = ProductForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)


    def test_register_form_data(self):
        form = RegisterForm(data={
            "username": "Muzammil",
            "password": "testmuzammil",
            "confirm_password": "testmuzammil",
            "first_name": "Muzammil",
            "last_name": "Ahmadzai",
            "email": "muzammilahmadzai78@gmail.com"
        })
        self.assertTrue(form.is_valid())

    def test_register_form_no_data(self):
        form = RegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)


    def test_profile_form_data(self):
        form = ProfileForm(data={
            "phone_number": "0738394839"
        })

        self.assertTrue(form.is_valid())


    def test_profile_form_no_data(self):
        form = ProfileForm(data={})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 0)