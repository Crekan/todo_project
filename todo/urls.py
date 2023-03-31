from django.urls import path

from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete

app_name = 'todo'

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('create/', TaskCreate.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdate.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
]
