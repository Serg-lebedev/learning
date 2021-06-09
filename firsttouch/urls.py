from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bboard/', include("bboard.urls")),
    path('accounts/login/', LoginView.as_view(), name='login')
]