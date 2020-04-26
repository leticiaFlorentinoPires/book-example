from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^$', views.send_login_email, name='send_email'),
    url(r'^$', views.login, name='login_email'),
]
