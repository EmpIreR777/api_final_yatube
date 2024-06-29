from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',)
    slug = models.SlugField(
        unique=True,
        verbose_name='slug',)
    description = models.TextField(
        verbose_name='Описание',)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True, blank=True,
        verbose_name='Картинка',
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts',
        blank=True, null=True,
        verbose_name='Группа',
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост',
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',)
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Подписан',)

    def __str__(self):
        return f'{self.user}'
