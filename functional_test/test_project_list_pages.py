from selenium import webdriver
from invapp.models import Product, Profile
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from django.test import Client


class TestProjectListPage(StaticLiveServerTestCase):
    def setUp(self):
        service = Service('functional_test/chromedriver.exe')
        self.browser = webdriver.Chrome(service=service)

        self.user = User.objects.create_user(username="testuser", password="testpassword")
        


    def tearDown(self):
        self.browser.close()

    def login(self):
        self.browser.get(self.live_server_url)

        self.browser.find_element(By.NAME, 'username').send_keys('testuser')
        self.browser.find_element(By.NAME, 'password').send_keys('testpassword')
        self.browser.find_element(By.TAG_NAME, 'button').click()

    def test_no_project_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        alert = self.browser.find_element(By.CLASS_NAME, 'login-form-container')
        self.assertEqual(
            alert.find_element(By.TAG_NAME, 'h1').text, 'Login'  
        )

    def test_no_project_alert_a_tag_redirected_to_register_page(self):
        self.browser.get(self.live_server_url)
        add_url = self.live_server_url + reverse('register')
        self.browser.find_element(By.TAG_NAME, 'a').click()

        self.assertEqual(
            self.browser.current_url,
            add_url
        )
    



    def test_user_product_list(self):
            product = Product.objects.create(
                user = self.user,
                name = "Book",
                sku = "B42", 
                price = "149",
                quantity = 200,
                supplier = "Aksos",
                category = "accessories"
            )
            self.login()

            self.browser.get(self.live_server_url)
            self.browser.find_element(By.CLASS_NAME, 'show-product').click()
            final = self.browser.find_element(By.CLASS_NAME, 'table-container')

            self.assertEqual(
                final.find_element(By.CLASS_NAME, 'product-name').text, "Book")


    def test_user_product_detail_view_button(self):
         product = Product.objects.create(
              user = self.user,
              name = "Game",
              sku = "G03",
              price = 200,
              quantity = 20,
              supplier = "CallOfDuty",
              category = "computers"
         )
         self.login()

         self.browser.get(self.live_server_url)
         self.browser.find_element(By.CLASS_NAME, 'show-product').click()
         self.browser.find_element(By.CLASS_NAME, 'detail-product').click()
         detail_url = self.live_server_url + reverse('detail', args=[1])

         self.assertEqual(
              self.browser.current_url, detail_url
         )

    def test_login_page(self):
         self.browser.get(self.live_server_url)
         self.browser.find_element(By.NAME, 'username').send_keys('testuser')
         self.browser.find_element(By.NAME, 'password').send_keys('testpassword')
         self.browser.find_element(By.TAG_NAME, 'button').click()
         home_url = self.live_server_url + reverse('home')

         self.assertEqual(
              self.browser.current_url, home_url
         )

     
    def test_register_form_page(self):
         self.browser.get(self.live_server_url)
         self.browser.find_element(By.TAG_NAME, 'a').click()
         self.browser.find_element(By.NAME, "username").send_keys('ahmad')
         self.browser.find_element(By.NAME, 'password').send_keys('work')
         self.browser.find_element(By.NAME, 'confirm_password').send_keys('work')
         self.browser.find_element(By.NAME, 'first_name').send_keys('Ahmad')
         self.browser.find_element(By.NAME, 'last_name').send_keys('khan')
         self.browser.find_element(By.NAME, 'email').send_keys('ahmad353@gmail.com')
         self.browser.find_element(By.TAG_NAME, 'button').click()
         home_url = self.live_server_url + reverse('home')

         self.assertEqual(
              self.browser.current_url, home_url
         )

        
        