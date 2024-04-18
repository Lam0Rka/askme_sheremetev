from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    image = models.ImageField(null=True, blank=True)
    rating = models.IntegerField(default=0)
    def str(self):
        return self.user.username


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag_name


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=300)
    question_field = models.TextField(max_length=5000)
    rating = models.IntegerField(null=True)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_field = models.TextField(max_length=5000)
    is_true = models.BooleanField()
    rating = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.answer_field


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_true = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
