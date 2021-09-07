from django.urls import path
from .views import CustomUserCreate, BlackListTokenView

app_name='users'

urlpatterns = [
  path('register/', CustomUserCreate.as_view(), name="create_user"),
  path('logout/blakclist/', BlackListTokenView.as_view(), name='blacklist'),
]

