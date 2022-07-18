from django.contrib import admin
from apps.posts.models import Post, PostImage, FavoritePost


class ProductImageAdmin(admin.TabularInline):
    model = PostImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    prepopulated_fields = {"slug" : ("title", )}

admin.site.register(Post, ProductAdmin)
admin.site.register(FavoritePost)
