from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def get_hot(self):
        return self.annotate(answers_count=models.Count('answer',  distinct=True),
            question_likes_count=models.Count('questionlike',  distinct=True)).order_by('-question_likes_count')

    def get_new(self):
        return self.annotate(answers_count=models.Count('answer',  distinct=True),
            question_likes_count=models.Count('questionlike',  distinct=True)).order_by('-created_at')

    def get_by_tag(self, tag_name):
        self = self.answers_count()
        return self.filter(tags__name=tag_name).annotate(question_likes_count=models.Count('questionlike',  distinct=True)).order_by(
            'created_at')

    def answers_count(self):
        return self.get_queryset().annotate(answers_count=models.Count('answer',  distinct=True))

    def question_likes_count(self):
        return self.get_queryset().annotate(question_likes_count=models.Count('questionlike'))

    def answer_likes_count(self):
        return self.get_queryset().annotate(answer_likes_count=models.Count('answerlike'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    image = models.ImageField(default='static/img/img.png', blank=True, null=True)
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
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QuestionManager()


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

class QuestionLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_true = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'question')


class AnswerLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_true = models.BooleanField()
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('user', 'answer')

