from django.urls import include, path

from .views import CustomAuthToken, Logout

urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/token/login/',
         CustomAuthToken.as_view(), name='login'),
    path('auth/token/logout/',
         Logout.as_view(), name='logout')
]
