from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserChangeForm
from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.forms import ModelForm


class ProfileUpdateForm(ModelForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]  # username


def add_to_group(user):
    group = Group.objects.get(name='common')
    group.user_set.add(user)


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        add_to_group(user)
        return user


class BasicSocialSignupForm(SocialSignupForm):

    def save(self, request):
        user = super(BasicSocialSignupForm, self).save(request)
        add_to_group(user)
        return user
