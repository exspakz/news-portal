from django.core.cache import cache
from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    rating = models.SmallIntegerField(default=0)

    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        post_rating = self.post_set.aggregate(Sum('rating')).get('rating__sum')
        if post_rating is None:
            post_rating = 0

        comment_rating = self.authorUser.comment_set.aggregate(Sum('rating')).get('rating__sum')
        if comment_rating is None:
            comment_rating = 0

        compost_rating = Comment.objects.filter(commentPost__postAuthor=self).aggregate(Sum('rating')).get('rating__sum')
        if compost_rating is None:
            compost_rating = 0

        self.rating = post_rating * 3 + comment_rating + compost_rating
        self.save()

    def __str__(self):
        return f'{self.authorUser.username}'


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User, through='SubscribeCategory')

    def get_subscribers(self):
        return ",\n".join([str(p) for p in self.subscribers.all()])

    def __str__(self):
        return f'{self.name}'


class SubscribeCategory(models.Model):
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)
    userThrough = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.userThrough.username} / {self.categoryThrough.name}'


class Post(models.Model):
    NEWS = 'NW'
    ARTICLES = 'AR'
    CATEGORIES = [
        (NEWS, _('News')),
        (ARTICLES, _('Article')),
    ]

    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)
    dateCreation = models.DateTimeField(auto_now_add=True)
    categoryType = models.CharField(max_length=2, choices=CATEGORIES, default=ARTICLES)

    postAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    postCategory = models.ManyToManyField(Category, through='PostCategory')

    def __str__(self):
        return f'{self.title.title()}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.id}')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[:124]}...'


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.postThrough.title} / {self.categoryThrough.name}'


class Comment(models.Model):
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)
    dateCreation = models.DateTimeField(auto_now_add=True)

    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
