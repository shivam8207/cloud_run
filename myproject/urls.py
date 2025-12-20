from django.contrib import admin
from django.urls import path
from myapp.views import product_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_page),
]

