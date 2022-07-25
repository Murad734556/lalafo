from django import forms
from django.contrib import admin
from apps.posts.models import Post, PostImage, FavoritePost
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


class PostAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget)
    description_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget)


# @admin.register(Post)
# class PostAdmin(TranslationAdmin):
#     list_display= ("user", "title", "description", "category", "slug",)


class ProductImageAdmin(admin.TabularInline):
    model = PostImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    prepopulated_fields = {"slug" : ("title", )}

admin.site.register(Post, ProductAdmin)
admin.site.register(FavoritePost)
