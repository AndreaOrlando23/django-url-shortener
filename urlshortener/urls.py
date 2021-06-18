from django.urls import	path
from .views import home_view


appname = "shortener" # namespacing

urlpatterns = [
	path("", home_view, name="home"),
]
