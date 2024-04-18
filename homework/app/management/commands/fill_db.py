from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from app import models
import random
import string

class Command(BaseCommand):
    help = 'Fill Database'
    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Ratio dependences on count of users/questions/answers and etc')

    def handle(self, *args, **kwargs):
        ratio = kwargs['ratio']

        users_count = ratio
        questions_count = ratio * 10
        answers_count = ratio * 100
        tags_count = ratio
        likes_count = ratio * 200


        self.create_users(users_count)
        self.create_tags(tags_count)
        self.create_questions(questions_count)
        self.create_answers(answers_count)
        self.create_likes(likes_count)

    # done
    def create_users(self, count):
        print('Creating users')
        names = [User(username=f'User_{i}', email=f'User_{i}@example.com', password=f'Password{i}', first_name=f'Name {i}') for i in range (count)]
        User.objects.bulk_create(names)
        # models.Profile.objects.bulk_create(user=user)
        print('Finish creating users')

    # done
    def create_tags(self, count):
        print('Creating tags')
        tags = [models.Tag(tag_name=f'Tag {i}') for i in range (count)]
        models.Tag.objects.bulk_create(tags)
        print('Finish creating tags')

    def create_questions(self, count):
        print('Creating questions')
        users = User.objects.all() #.exclude(is_superuser=True)
        tagss = models.Tag.objects.all()
        questions = [models.Question(user=random.choice(users),rating=random.randrange(500), question_title=f'Title {i}', question_field=f'Field {i}', tags=random.choice(tagss)) for i in range (count)]
        q_instance = models.Question.objects.bulk_create(questions)
        print('Finish creating questions')

    def create_answers(self, count):
        print('Creating answers')
        users = User.objects.all()
        questions = models.Question.objects.all() #.exclude(is_superuser=True)
        answers = [models.Answer(user=random.choice(users), question=random.choice(questions),rating=random.randrange(500), answer_field=f'Field {i}', is_true=random.randrange(2)) for i in range (count)]
        models.Answer.objects.bulk_create(answers)
        print('Finish creating ansers')

    def create_likes(self, count):
        print('Creating likes')
        users = User.objects.all()
        questions = models.Question.objects.all()
        answers = models.Answer.objects.all() #.exclude(is_superuser=True)
        answers = [models.Like(user=random.choice(users), question=random.choice(questions), answer=random.choice(answers), is_true=random.randrange(2)) for i in range (count)]
        models.Like.objects.bulk_create(answers)
        print('Finish creating likes')
