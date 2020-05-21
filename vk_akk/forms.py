from django import forms

from vk_akk.models import VkAkk


class AuthForm(forms.Form):
    akk_id = forms.CharField()


class AkksAddForm(forms.Form):
    akks = forms.CharField()


class AddAkkGroupForm(forms.Form):
    group_name = forms.CharField()
    akks = forms.CharField()


# class AkkModelForm(forms.ModelForm):
#     class Meta:
#         model = VkAkk
#         fields = ['vk_akks_group', 'vk_users_group', 'follow_number', 'user']