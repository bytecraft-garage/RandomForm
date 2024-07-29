from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name ="home"),
    path('panel/',views.panel, name = "panel"),
    path('delete/<id>',views.delete, name ="delete")
]