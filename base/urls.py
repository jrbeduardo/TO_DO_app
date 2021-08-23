from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns=[
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('create_task/', TaskCreate.as_view(), name='task_create'),
    path('update_task/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('delete_task/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
]
