from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

# Create your tests here.


class TestUserAuthentication(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_login_page_exist(self):
        self.browser.get(self.live_server_url+'/account/login')
        body = self.browser.find_element_by_tag_name("body")
        self.assertIn('Login', body.text)

    def test_signup_page_exist(self):
        self.browser.get(self.live_server_url+'/account/signup')
        body = self.browser.find_element_by_tag_name("body")
        self.assertIn('Register', body.text)
