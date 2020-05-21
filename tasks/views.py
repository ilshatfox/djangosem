from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView

from tasks.forms import CreateTaskForm, StartFollowTaskForm, CreateTaskForm2
from tasks.models import FollowTask
from tasks.service import create_follow_task, start_follow_task_with_id
from vk_akk.models import VkAkksGroup
from vk_users.models import VkUsersGroup


class FollowTaskList(LoginRequiredMixin, ListView):
    model = FollowTask
    template_name = 'task/task_view.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class AddFollowTask(LoginRequiredMixin, ListView):
    model = FollowTask
    template_name = 'task/add_follow_task_view.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super(AddFollowTask, self).get_context_data(**kwargs)
        context.update({
            'vk_akk_groups': VkAkksGroup.objects.filter(user=self.request.user),
            'vk_users_groups': VkUsersGroup.objects.filter(user=self.request.user),
            'form': CreateTaskForm2()
        })
        return context

    def post(self, request):
        form = CreateTaskForm2(request.POST)
        if form.is_valid():
            # form
            form.save()
            # vk_akk_group_id = form.cleaned_data['vk_akk_group_id']
            # vk_users_group_id = form.cleaned_data['vk_users_group_id']
            # follow_number = form.cleaned_data['follow_number']
            # print('vk_akk_group_id', vk_akk_group_id)
            # print('vk_users_group_id', vk_users_group_id)
            # # input('ff')
            # results = create_follow_task(vk_akks_group_id=int(vk_akk_group_id), vk_users_group_id=int(vk_users_group_id), follow_number=follow_number, user=request.user)
            results = []
            template = 'results.html'
            context = {'messages': results}
            return render(request, template, context)


class StartFollowTask(LoginRequiredMixin, ListView):
    model = FollowTask
    template_name = 'task/start_follow_task.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def post(self, request):
        form = StartFollowTaskForm(request.POST)
        if form.is_valid():
            follow_task_id = form.cleaned_data['follow_task_id']
            results = start_follow_task_with_id(follow_task_id)
            template = 'results.html'
            context = {'messages': results}
            return render(request, template, context)
