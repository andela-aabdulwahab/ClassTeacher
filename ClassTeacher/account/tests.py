from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.contrib.auth.models import User

# Create your tests here.


class TestUserAuthentication(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.implicitly_wait(3)
        user = User.objects.create_user(username="malik", password="malikwahab")
        user.save()

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

    def test_user_can_login(self):
        self.browser.get(self.live_server_url+'/account/login')

        # find username
        username = self.browser.find_element_by_name("username")
        username.send_keys("malik")

        # find password
        password = self.browser.find_element_by_name("password")
        password.send_keys("malikwahab")

        # find submit botton
        submit = self.browser.find_element_by_name("submit")
        submit.click()

        body = self.browser.find_element_by_tag_name("body")

        # assert login success_url and user redirected
        self.assertNotIn("Login", body.text)

    def test_user_invalid_login_fails(self):
        self.browser.get(self.live_server_url+'/account/login')

        # find username
        username = self.browser.find_element_by_name("username")
        username.send_keys("nouser")

        # find password
        password = self.browser.find_element_by_name("password")
        password.send_keys("nouser")

        # find submit botton
        submit = self.browser.find_element_by_name("submit")
        submit.click()

        body = self.browser.find_element_by_tag_name("body")

        # assert login success_url and user redirected
        self.assertIn("Login", body.text)

    def test_user_can_signup(self):
        self.browser.get(self.live_server_url+'/account/signup')

        # find username
        # find username
        username = self.browser.find_element_by_name("username")
        username.send_keys("adeyi")

        # find password1
        password = self.browser.find_element_by_name("password2")
        password.send_keys("malikwahab")

        # find password2
        password = self.browser.find_element_by_name("password2")
        password.send_keys("malikwahab")

        # find submit botton
        submit = self.browser.find_element_by_name("submit")
        submit.click()

        body = self.browser.find_element_by_tag_name("body")

        # assert login success_url and user redirected
        self.assertIn("Register", body.text)


    def test_invalid_signup_fails(self):
        self.browser.get(self.live_server_url+'/account/signup')

        # find username
        # find username
        username = self.browser.find_element_by_name("username")
        username.send_keys("malik")

        # find password1
        password = self.browser.find_element_by_name("password2")
        password.send_keys("malikwahab")

        # find password2
        password = self.browser.find_element_by_name("password2")
        password.send_keys("malikwahab")

        # find submit botton
        submit = self.browser.find_element_by_name("submit")
        submit.click()

        body = self.browser.find_element_by_tag_name("body")

        # assert login success_url and user redirected
        self.assertIn("Register", body.text)
