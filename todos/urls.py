from django.urls import path
from .views import GroupList, TaskList, TaskDetail

app_name='todos'

urlpatterns = [
    path('task/<str:pk>/', TaskList.as_view()),
    path('group/', GroupList.as_view()),
    path('task/detail/<str:pk>/', TaskDetail.as_view()),
]

