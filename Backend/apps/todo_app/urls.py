from django.urls import path
from .views import TaskListView, TaskView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/get/<int:pk>/', TaskView.as_view(), name='task-details'),
    path('tasks/create/', TaskView.as_view(), name="task-Create"),
    path('tasks/update/<int:pk>/', TaskView.as_view(), name='task-update'),
    path('tasks/delete/<int:pk>/', TaskView.as_view(), name='task-delete' )

]

