from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import (
    Author, Category, Post, PostCategory, SubscribeCategory, Comment
)


class PostCategoryInLine(admin.TabularInline):
    model = PostCategory
    fk_name = 'postThrough'
    extra = 1


class PostAdmin(TranslationAdmin):
    inlines = [PostCategoryInLine]

    list_display = (
        'title', 'rating', 'dateCreation', 'categoryType', 'postAuthor',
    )
    list_filter = ('categoryType', 'postAuthor', 'postCategory', )
    search_fields = ('title', )


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('postThrough', 'categoryThrough', )
    list_filter = ('categoryThrough', )


class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'get_subscribers', )


admin.site.register(Author, )
admin.site.register(Category, CategoryAdmin, )
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin, )
admin.site.register(Comment, )
admin.site.register(SubscribeCategory, )