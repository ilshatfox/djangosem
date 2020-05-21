from django import forms

from tasks.models import FollowTask


# class CreateTaskForm(forms.ModelForm):
#     class Meta:
#         model = FollowTask
#         fields = ['vk_akks_group', 'vk_users_group']

class CreateTaskForm2(forms.ModelForm):
    class Meta:
        model = FollowTask
        fields = ['vk_akks_group', 'vk_users_group', 'follow_number', 'user', 'is_fast_follow']


class CreateTaskForm(forms.Form):
    vk_akk_group_id = forms.CharField()
    vk_users_group_id = forms.CharField()
    follow_number = forms.IntegerField()


class StartFollowTaskForm(forms.Form):
    follow_task_id = forms.CharField()
