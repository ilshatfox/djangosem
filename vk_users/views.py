from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import ListView, TemplateView

from vk_users.forms import VkUsersGroupAddForm, VkFileUsersForm
from vk_users.models import VkUsersGroup, VkFileUsers, VkNews
from vk_users.service import add_users_group


class UserGroupsView(ListView):
    model = VkUsersGroup
    template_name = 'vk_users/users_group_view.html'
    context_object_name = 'users_groups'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class AddUserGroupView(LoginRequiredMixin, TemplateView):
    template_name = 'vk_users/add_users_group.html'

    def post(self, request):
        form = VkUsersGroupAddForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data['group_name']
            users = form.cleaned_data['users']
            results = add_users_group(users.split('\n'), group_name, request.user)
            template = 'results.html'
            context = {'messages': results}
            return render(request, template, context)


def upload_file(request):
    if request.method == 'POST':
        print('123fff')
        form = VkFileUsersForm(request.POST, request.FILES)

        if form.is_valid():
            print('222ff11')
            filename = form.cleaned_data['name']
            file = request.FILES['file']
            user = request.user
            VkFileUsers.write_file(filename, file, user)
            # handle_uploaded_file(request.FILES['file'])
            return redirect('/')
    else:
        form = VkFileUsersForm()
    return render(request, 'vk_users/test_upload.html', {'form': form})


class MyFilesView(LoginRequiredMixin, ListView):
    model = VkFileUsers
    template_name = 'vk_users/test_files.html'
    context_object_name = 'files'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class NewsView(LoginRequiredMixin, ListView):
    model = VkNews
    template_name = 'vk_users/vk_news.html'
    context_object_name = 'files'


class TargetNewsView(LoginRequiredMixin, View):
    template_name = 'vk_users/vk_target_news.html'

    def get(self, request, news_id):
        try:
            news = VkNews.objects.get(id=int(news_id))
        except:
            news = None
        return render(request, self.template_name, {'news': news})


