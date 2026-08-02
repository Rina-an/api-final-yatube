from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import DEFAULT_TEXT_LENGTH

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="Идентификатор")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title[:DEFAULT_TEXT_LENGTH]


class Post(models.Model):
    text = models.TextField(verbose_name="Текст")
    pub_date = models.DateTimeField('Дата публикации',
                                    auto_now_add=True
                                    )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name="Автор публикации"
                               )
    image = models.ImageField(upload_to='posts/',
                              verbose_name="Изображение",
                              null=True,
                              blank=True
                              )
    group = models.ForeignKey(Group,
                              verbose_name="Группа",
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True
                              )

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"
        default_related_name = 'posts'
        ordering = ['pub_date']

    def __str__(self):
        return self.text[:DEFAULT_TEXT_LENGTH]


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name="Автор комментария"
                               )
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             verbose_name="Пост"
                             )
    text = models.TextField(verbose_name="Текст комментария")
    created = models.DateTimeField('Дата добавления',
                                   auto_now_add=True,
                                   db_index=True
                                   )

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"
        default_related_name = 'comments'

    def __str__(self):
        return f"Комментарий от {self.author.username} к посту '{self.post}'"


class Follow(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name="Автор",
                             related_name='follows',
                             )
    following = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  verbose_name="Подписчик",
                                  related_name='following',
                                  )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "following"], name="unique_user_following"
            )
        ]

    def __str__(self):
        return f"{self.user.username} подписан на {self.following.username}"
