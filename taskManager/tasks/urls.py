from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.allTasks, name="tasks"),
    path('<int:id>/delete', views.TaskDelete.as_view(), name="delete"),
    path('<int:id>/edit', views.edit, name="edit"),
    path('create', views.TasksCreate.as_view(), name="create"),
]