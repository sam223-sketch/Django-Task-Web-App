from django.urls import path

from . import views 

app_name = "Tasks" #gives unique identity to app urls
urlpatterns = [
	  path("", views.index, name = "index"),
	  path("add", views.add, name = "add")
]