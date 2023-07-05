from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect, render
from django.urls import reverse

from news.models import Author, Category
from .forms import ProfileUpdateForm
from .mixins import ProfileRequiredMixin


class UserProfileUpdate(ProfileRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'account/profile_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.request.user.groups.filter(name='authors').exists()
        return context

    def get_success_url(self):
        return reverse('account_profile', kwargs={'pk': self.kwargs['pk']})


@login_required
def upgrade_user(request):
    user = request.user
    group = Group.objects.get(name='authors')
    if not user.groups.filter(name='authors').exists():
        group.user_set.add(user)
        if not hasattr(user, 'author'):
            Author.objects.create(authorUser=user)
    return redirect('/')


@login_required
def add_subscribe(request, **kwargs):
    category = Category.objects.get(pk=int(kwargs['pk']))
    category.subscribers.add(request.user, through_defaults=None)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_subscribe(request, **kwargs):
    category = Category.objects.get(pk=int(kwargs['pk']))
    category.subscribers.remove(request.user)
    return redirect(request.META.get('HTTP_REFERER'))
