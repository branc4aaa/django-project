from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/new', views.newTask, name='nt'),
    path('', views.message, name='registration_success'),
    path('tasks/update/<int:tid>/', views.updateTask_view, name='update_task'),
    path('logout/', views.logout_view, name='logout'),
    path('tasks/delete/<int:tid>/', views.deleteTask_view, name='delete_task'),
    
]
