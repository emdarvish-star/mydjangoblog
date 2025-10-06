from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('singup',views.singup_view,name = 'singup'),
]
