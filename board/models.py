from django.db import models
from accounts.models import User

# Create your models here.
class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='board', null=True)
    title = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='board/', null=True)
    context = models.TextField()
    created_at = models.DateField(auto_created=True, null=True)
    liked_user = models.ManyToManyField(User, through='Like', related_name='likes')
    slug = models.SlugField(max_length=100, allow_unicode=True, null=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.liked_user

    def get_comments(self):
        return self.comment.filter(parent_comment=None)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
    article = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='like_board')

    class Meta:
        unique_together = ('user', 'article')


class Comment(models.Model):
    article = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comment')
    content = models.TextField(null=False)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True) # 1:N의 관계. 대댓글이 아닌 경우에는 null값이 생기니 True로 설정.

    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['created_at']

    def get_comments(self):
        return Comment.objects.filter(parent_comment=self).filter(active=True)