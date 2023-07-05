from django.forms import DateInput, DateTimeInput
from django.utils.translation import gettext_lazy as _

import django_filters
from django_filters import FilterSet

from .models import Author, Post, Category


class PostFilter(FilterSet):

    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label=_('Title'),
    )

    date = django_filters.DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label=_('Date'),
        widget=DateTimeInput(
            attrs={'type': 'date'},
            format='%Y-%m-%dT',
        ),
    )

    author = django_filters.ModelChoiceFilter(
        field_name='postAuthor',
        queryset=Author.objects.all(),
        label=_('Author'),
        empty_label=_('Select a author'),
    )

    category = django_filters.ModelChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label=_('Category'),
        empty_label=_('Select a category'),
    )

    type = django_filters.ChoiceFilter(
        field_name='categoryType',
        label=_('Type'),
        empty_label=_('Select a type'),
        choices=Post.CATEGORIES,
    )
