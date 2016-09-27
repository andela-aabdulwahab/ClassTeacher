from django.conf.urls import url
from account.views import LoginView, RegisterView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^signup/$', RegisterView.as_view(), name="signup"),
]
