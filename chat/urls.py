from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^registration$', views.RegView.as_view(), name='registration'),
]
