from django import forms

from proxies.models import Proxy


class ProxyForm(forms.ModelForm):
    class Meta:
        model = Proxy
        fields = ['ip', 'port', 'login', 'password', 'type', 'user']


class ProxyLineForm(forms.Form):
    proxies = forms.CharField()
