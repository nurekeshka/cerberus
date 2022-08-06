from django.contrib import admin
from django.urls import path
from passwords import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PasswordsView.as_view(), name='passwords')
]
