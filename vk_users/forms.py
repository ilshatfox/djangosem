from django import forms


class VkUsersGroupAddForm(forms.Form):
    group_name = forms.CharField()
    users = forms.CharField()


class VkFileUsersForm(forms.Form):
    name = forms.CharField(max_length=50)
    file = forms.FileField()
