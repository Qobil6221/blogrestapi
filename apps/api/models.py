from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db.models import Model, DateTimeField, CharField, EmailField, TextField, BooleanField, ForeignKey, CASCADE, \
    DO_NOTHING, ManyToManyField
from django.forms import DateField


class AbstractModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    birthday = DateField()
    bio = TextField()


class Post(AbstractModel):
    title = CharField(max_length=128)
    body = TextField()
    is_active = BooleanField(default=True)
    user_id = ForeignKey(User, CASCADE, related_name='posts')

    def __str__(self):
        return self.title


class Comment(AbstractModel):
    body = TextField()
    post_id = ForeignKey(Post, on_delete=CASCADE, related_name='comments')
    user_id = ForeignKey(User, on_delete=CASCADE, related_name='comments')


class Like(AbstractModel):
    user_id = ForeignKey(User, DO_NOTHING, related_name='likes')
    post_id = ForeignKey(Post, CASCADE, related_name='likes')
    comment = ForeignKey(Comment, on_delete=CASCADE, related_name='likes')
