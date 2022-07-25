from modeltranslation.translator import register, TranslationOptions
from apps.categories.models import Category
from apps.posts.models import Post
from apps.settings.models import Setting,  Contact, Blog


# @register(Category)
# class CategoryTranslationOptions(TranslationOptions):
#     fields=("title")

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields=("user","title","description", "category", "slug", "valid",)

@register(Setting)
class SettingTranslationOptions(TranslationOptions):
    fields=("title","description", "address" )

# @register(AboutUs)
# class AboutUsTranslationOptions(TranslationOptions):
#     fields=("description")

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields=("name","title","problem", "status")

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields=("title","description" )