from django.test import TestCase, client
from django.urls import reverse, resolve
from invapp.models import Product, Profile
from django.contrib.auth.models import User


class TestView(TestCase):
    def setUp(self):
        self.home_url = reverse('home')
        self.product_url = reverse('product_list')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.register_url = reverse('register')
        self.profile_url = reverse('profile')
        self.user = User.objects.create_user(password="testpassword", username="username")
        self.profile = Profile.objects.create(user=self.user)
        self.Product = Product.objects.create(
            user=self.user,
            name = "Shirt",
            sku = "S20",
            price = 20,
            quantity = 30,
            supplier = 'Gucci',
            category = "computers"
        )
        self.client.force_login(self.user)
        self.update_url = reverse('update', args=[self.Product.product_id])
        self.delete_url = reverse('delete', args=[self.Product.product_id])
        self.detail_url = reverse('detail', args=[self.Product.product_id])
        self.create_url = reverse('create')
    def test_home_view_GET(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'invapp/home.html')
    def test_read_view_GET(self):
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'invapp/product_list.html')

    def test_login_view_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'invapp/login.html')

    def test_logout_view_GET(self):
        response  = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)

    def test_register_view_GET(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'invapp/register.html')

    def test_profile_view_GET(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'invapp/profile.html')

    def test_detail_view_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'invapp/detail.html')

    def test_update_view_GET(self):
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'invapp/product_form.html')

    def test_delete_view_GET(self):
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'invapp/product_confirm_delete.html')

    def test_add_product_view_GET(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'invapp/product_form.html')

    def test_add_product_view_POST(self):
        response = self.client.post(self.create_url, {
            "name": "loptop",
            "sku": "T04",
            "price": 200,
            "quantity": 9,
            "supplier": "Dell",
            "category": "computers"
        })

        product = Product.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(product.name, "Shirt")
        self.assertEqual(product.sku, "S20")
        self.assertEqual(product.user, self.user)

    def test_add_product_POST_no_data(self):
        response = self.client.post(self.create_url)
        product = Product.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(product, 1)

    def test_delete_product_POST_(self):
        response = self.client.post(self.delete_url)
        product = Product.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(product, 0)

    def test_update_product_POST(self):
        response = self.client.post(self.update_url, {
            "name": "Couch",
            "sku": "C20",
            "price": 200,
            "quantity": 40,
            "supplier": "Addidas",
            "category": "furniture"
        })

        self.assertEqual(response.status_code, 302)
    def test_update_product_POST_no_data(self):
        response = self.client.post(self.update_url)

        self.assertEqual(response.status_code, 200)


    def test_register_account_view_POST(self):
        response = self.client.post(self.register_url, {
            "username": "testuser",
            "password": "testpassword",
            "confirm_password": "testpassword",
            "first_name": "Muzammil",
            "last_name": "Ahmadzai",
            "email": "muzammilahmadzai78@gmail.com"
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(Profile.objects.count(), 2)

    def test_register_account_view_POST_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 200)

    def test_logout_view_POST(self):
        response = self.client.post(self.logout_url, {
            'username': 'username',
            'password': 'testpassword'
        })

        self.assertEqual(response.status_code, 302)
        self.assertFalse('__auth_user_id' in self.client.session)

    def test_login_view_POST(self):
        response = self.client.post(self.login_url, {
            'username': 'username',
            'password': 'testpassword'
        })

        self.assertEqual(response.status_code, 302)
        self.assertIsNotNone(self.client.session.get('_auth_user_id'))