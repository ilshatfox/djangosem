from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, FormView

from proxies.forms import ProxyLineForm, ProxyForm
from proxies.models import Proxy
from proxies.service import add_proxies
from vk_bot.base.status import Status


class ProxiesList(LoginRequiredMixin, ListView):
    model = Proxy
    template_name = 'proxy/proxy_view.html'
    context_object_name = 'proxies'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class AddProxies(LoginRequiredMixin, View):
    template_name = 'proxy/add_proxies.html'

    def get(self, request):
        return render(request, self.template_name, {'form': ProxyForm()})

    # def get_context_data(self, **kwargs):
    #     context = super(AddProxies, self).get_context_data(**kwargs)
    #     context.update({'form': ProxyForm()})

    def post(self, request):
        form = request.POST
        form = ProxyForm(form)
        if form.is_valid():
            form.save()
            # proxies = form.cleaned_data['proxies']
            # lines = proxies.split('\n')
            # results = add_proxies(lines, request.user)
            results = [Status(True, "Успешно добавил")]
            template = 'results.html'
            context = {'messages': results}
            return render(request, template, context)
        else:
            results = [Status(True, "Не удалось добавить!")]
            template = 'results.html'
            context = {'messages': results}
            return render(request, template, context)



# class AddProxies(FormView):
#     template_name = 'proxy/add_proxies.html'
#     form_class = ProxyLineForm
#     success_url = reverse_lazy('proxies:proxy_list')
#
#     def form_valid(self, form):
#         proxies = form.cleaned_data['proxies']
#         lines = proxies.split('\n')
#         add_proxies(lines)
#         return super().form_valid(form)