from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.contrib.auth.models import User
import time

# Create your tests here.


class TestClassList(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.implicitly_wait(3)
        user = User.objects.create_user(username="malik",
                                        password="malikwahab")
        user.save()
        self.browser.get(self.live_server_url+'/account/login')
        username = self.browser.find_element_by_name("username")
        username.send_keys("malik")
        password = self.browser.find_element_by_name("password")
        password.send_keys("malikwahab")
        submit = self.browser.find_element_by_name("submit")
        submit.click()

    def tearDown(self):
        self.browser.quit()

    def test_class_list_url_exit(self):
        self.browser.get(self.live_server_url+'/class/')
        body = self.browser.find_element_by_tag_name("body")
        self.assertIn('Class List', body.text)

    def test_class_create_url_exit(self):
        self.browser.get(self.live_server_url+'/class/new')
        body = self.browser.find_element_by_tag_name("body")
        self.assertIn("Create Class", body.text)

    def test_create_form_present(self):
        self.browser.get(self.live_server_url+'/class/new')
        body = self.browser.find_element_by_tag_name("body")
        self.assertIn("Level", body.text)

    def test_create_class(self):
        self.browser.get(self.live_server_url+'/class/new')
        name = self.browser.find_element_by_name("name")
        name.send_keys('Gold')
        submit = self.browser.find_element_by_name("submit")
        submit.click()
        body = self.browser.find_element_by_tag_name("body")
        self.assertIn("Gold", body.text)

    def test_single_class_view(self):
        self.browser.get(self.live_server_url+'/class/new')
        name = self.browser.find_element_by_name("name")
        name.send_keys('Gold')
        submit = self.browser.find_element_by_name("submit")
        submit.click()

        class_link = self.browser.find_element_by_link_text("Gold")
        class_link.click()

        body = self.browser.find_element_by_tag_name("body")
        self.assertIn("Detail View", body.text)
