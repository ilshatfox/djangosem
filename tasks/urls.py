from django.urls import path

from tasks.views import FollowTaskList, AddFollowTask, StartFollowTask

app_name = 'tasks'
urlpatterns = [
    path('follow_tasks/', FollowTaskList.as_view(), name='follow_tasks'),
    path('add_follow_task/', AddFollowTask.as_view(), name='add_follow_task'),
    path('start_follow_task/', StartFollowTask.as_view(), name='start_follow_task')
]