from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

# Create your tests here.


class TestUserAuthentication(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = WebDriver()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_login_page_exist(self):
        self.browser.get('/account/login')
        body = self.browser.find_element_by_tag_name("body")
        self.assertIn('Login', body.text)

    def test_signup_page_exist(self):
        self.browser.get('/account/signup')
        body = self.browser.find_element_by_tag_name("body")
        self.assertIn('Register', body.text)
