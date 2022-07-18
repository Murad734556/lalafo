from distutils.command.upload import upload
from django.db import models
from apps.users.models import User
from apps.categories.models import Category
from django.db.models.signals import pre_save
from apps.posts.slug_generator import unique_slug_generators

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="post_category", blank = True, null = True)
    price = models.PositiveBigIntegerField()
    post_image = models.ImageField(upload_to = "post_image/")
    CHOICE_CURRENCY =(
        ('KGS', 'KGS'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
        ('Договорная', 'Договорная')
    )
    currency=models.CharField(max_length=100, choices=CHOICE_CURRENCY, default='Договорная')
    phone=models.CharField(max_length=100, default='+996 708 89 03 08')
    created = models.DateTimeField(auto_now_add=True)
    STATUS_POST = (
        ('Free', 'Free'),
        ('Pro', 'Pro'),)
    status = models.CharField(choices=STATUS_POST, max_length=10, default='Free')
    slug = models.SlugField(blank=True, null = True, unique = True, verbose_name="Человекопонятный URL (само генерация)")
    valid= models.BooleanField(default=True, verbose_name="Действителный")
    
    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

class PostImage(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name="image_post")
    image= models.ImageField(upload_to= "second_post_image/")

    class Meta:
        verbose_name= "Дополнительная фотография"
        verbose_name_plural= "Дополнительные фотографии"


class FavoritePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorite_user", verbose_name="Понравившиеся посты пользоваьелю")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="favorite_post", verbose_name="Понравившиеся пост")
    

    def __str__(self):
        return f"{self.user.username} {self.post.title} {self.id}"

    class Meta:
        verbose_name = "Понравился пост"
        verbose_name_plural = "Понравились посты"

def slag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)


pre_save.connect(slag_pre_save_receiver, sender=Post)
