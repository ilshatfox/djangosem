from django.urls import path, re_path

from vk_users.views import UserGroupsView, AddUserGroupView, upload_file, MyFilesView, NewsView, TargetNewsView

app_name = 'vk_users'
urlpatterns = [
    path('user_groups/', UserGroupsView.as_view(), name='user_groups'),
    path('add_user_groups/', AddUserGroupView.as_view(), name='add_user_groups'),
    path('upload_file/', upload_file, name='upload_file'),
    path('my_files/', MyFilesView.as_view(), name='my_files'),
    path('vk_news/', NewsView.as_view(), name='vk_news'),
    re_path(r'^news_id(?P<news_id>\d+)/$', TargetNewsView.as_view(), name='news_id')
]
