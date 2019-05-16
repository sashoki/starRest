from blog.models import UserProfile, Post
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    username = forms.CharField(label="User name")
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = self.cleaned_data.pop("password")
        if self.instance.id is None and password == '':
            self.add_error('password', forms.ValidationError('Required field'))
        if password != '':
            self.instance.set_password(password)
            self.instance.save()
        return cleaned_data

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        if commit:
            user.save()
        return user