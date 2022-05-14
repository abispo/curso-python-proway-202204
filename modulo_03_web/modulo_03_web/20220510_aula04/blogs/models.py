from django.db import models
from polls.models import Question


class Post(models.Model):
    question = models.OneToOneField(
        Question,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column="id",

    )
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.body


class Tag(models.Model):
    post = models.ManyToManyField(Post)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
