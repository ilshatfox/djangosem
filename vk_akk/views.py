import traceback

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, TemplateView

from vk_akk.forms import AuthForm, AkksAddForm, AddAkkGroupForm
from vk_akk.models import VkAkk, VkAkksGroup
from vk_akk.service import auth_vk_akk, add_akks, add_akks_group


class VkAkkList(LoginRequiredMixin, ListView):
    model = VkAkk
    template_name = 'vk_akk/akk_view.html'
    context_object_name = 'akks'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class AddVkAkks(LoginRequiredMixin, TemplateView):
    template_name = 'vk_akk/add_akks.html'

    def post(self, request):
        form = AkksAddForm(request.POST)
        if form.is_valid():
            akks = form.cleaned_data['akks']
            print(akks)
            results = add_akks(akks.split('\n'), request.user)
            template = 'results.html'
            context = {'messages': results}
            return render(request, template, context)


class AuthAkk(View):
    def post(self, request):
        form = AuthForm(request.POST)
        if form.is_valid():
            akk_id = form.cleaned_data['akk_id']
            print('akk_id', akk_id)
            try:
                auth_vk_akk(request.user, akk_id)
            except:
                print(traceback.format_exc())
                pass
            return redirect(reverse('index'))


class AkkGroupsList(LoginRequiredMixin, ListView):
    model = VkAkksGroup
    template_name = 'vk_akk/akk_groups_view.html'
    context_object_name = 'akk_groups'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class AddAkkGroups(LoginRequiredMixin, TemplateView):
    template_name = 'vk_akk/add_akks_group.html'

    def post(self, request):
        form = AddAkkGroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data['group_name']
            akks = form.cleaned_data['akks']
            akks = akks.replace('\r', '')
            print(akks)
            akks = akks.split('\n')
            akk_logins = [akk.split(':')[0] for akk in akks]
            results = add_akks_group(akk_logins, group_name, request.user)
            template = 'results.html'
            context = {'messages': results}
            return render(request, template, context)


# class VkAkkView(View):
#     def get(self, request):
#         template = ''
#         return render(request, template, {'form': AkkModelForm()})
#
#     def post(self, request):
