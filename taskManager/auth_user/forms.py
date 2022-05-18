from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from auth_user.models import UserProfile


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'

        self.fields['username'].widget.attrs['placeholder'] = 'Login'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'

        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'

    class Meta:
        model = UserProfile
        fields = ['phone']