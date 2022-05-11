from django.db import models
from polls.models import Question


class Post(models.Model):
    question = models.OneToOneField(
        Question, on_delete=models.CASCADE, primary_key=True
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
