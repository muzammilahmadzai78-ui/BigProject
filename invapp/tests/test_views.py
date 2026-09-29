from django.test import TestCase, Client
from invapp.models import Product, Profile
from django.urls import reverse, resolve
from django.contrib.auth.models import User


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.product_url = reverse('product_list')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.register_url = reverse('register')
        self.profile_url = reverse('profile')
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.profile = Profile.objects.create(user=self.user)
        self.product = Product.objects.create(
            user = self.user,
            name = "Test Product",
            sku = "S04",
            price = 30,
            quantity = 5,
            supplier = "Addidas",
            category = "computers"
        )
        self.client.force_login(self.user)
        self.detail_url = reverse('detail', args=[self.product.product_id])
        self.update_url = reverse('update', args=[self.product.product_id])
        self.delete_url = reverse('delete', args=[self.product.product_id])

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