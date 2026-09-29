from django.test import SimpleTestCase
from django.urls import reverse, resolve
from invapp.views import (
    home,
    create_home_view,
    create_read_view, 
    create_update_view, 
    create_delete_view, 
    create_product_detail,
    register_account,
    login_view,
    logout_view

)
class TestUrls(SimpleTestCase):
    def test_urls_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)


    def test_url_create(self):
        url = reverse('create')
        self.assertEqual(resolve(url).func, create_home_view)

    def test_url_read(self):
        url = reverse('product_list')
        self.assertEqual(resolve(url).func, create_read_view)

    def test_url_update(self):
        url = reverse('update', args=[5])
        self.assertEqual(resolve(url).func, create_update_view) 

    def test_url_delete(self):
        url = reverse('delete', args=[5])
        self.assertEqual(resolve(url).func, create_delete_view)

    def test_url_detail(self):
        url = reverse('detail', args=[5])
        self.assertEqual(resolve(url).func, create_product_detail)

    def test_url_register(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register_account)

    def test_url_login(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_view)

    def test_url_logout(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_view)