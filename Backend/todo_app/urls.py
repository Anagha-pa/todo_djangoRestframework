from django.urls import path
from .views import TaskListView,TaskDetailsView,TaskCreateView,TaskUpdateView,TaskDeleteView

urlpatterns = [
    path('task-list/',TaskListView.as_view(),name='task-list'),
    path('task-details/<int:pk>/',TaskDetailsView.as_view(),name='task-details'),
    path('task-create/', TaskCreateView.as_view(), name="task-Create"),
    path('task-update/<int:pk>/',TaskUpdateView.as_view,name='task-update'),
    path('task-delete/<int:pk>/',TaskDeleteView.as_view(),name='task-delete' )

]

