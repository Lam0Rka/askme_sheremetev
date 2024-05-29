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
        likes_count = ratio


        # self.create_users(users_count)
        # self.create_tags(tags_count)
        # self.create_questions(questions_count)
        # self.create_answers(answers_count)
        self.create_likes(likes_count)
        

    # done
    def create_tags(self, count):
        print('Creating tags')
        tags = [models.Tag(tag_name=f'Tag {i}') for i in range (count)]
        models.Tag.objects.bulk_create(tags)
        print('Finish creating tags')

    def choose_tags(self, tagss):
        a1 = random.choice(tagss)
        a2 = random.choice(tagss)
        a3 = random.choice(tagss)
        return a1, a2, a3
    

    def create_users(self, count):
        print('Creating users')
        names = [User(username=f'User_{i}', email=f'User_{i}@example.com', password=f'Password{i}', first_name=f'Name {i}') for i in range (count)]
        user = User.objects.bulk_create(names)
        # models.Profile.objects.bulk_create(user=user)
        print('Finish creating users')

    def create_questions(self, count):
        print('Creating questions')
        users = User.objects.all() 
        tagss = models.Tag.objects.all()
        
        questions = [models.Question(user=random.choice(users),rating=random.randrange(500), question_title=f'Title {i}', question_field=f'Field {i}') for i in range (count)]
        q_instance = models.Question.objects.bulk_create(questions)
        questions = models.Question.objects.all()

        for quest in questions:
            a1, a2, a3 = self.choose_tags(tagss)
            quest.tags.add(a1, a2, a3)

        print('Finish creating questions')

    def create_answers(self, count):
        print('Creating answers')
        users = User.objects.all()
        questions = models.Question.objects.all()
        answers = [models.Answer(user=random.choice(users), question=random.choice(questions),rating=random.randrange(500), answer_field=f'Field {i}', is_true=random.randrange(2)) for i in range (count)]
        models.Answer.objects.bulk_create(answers)
        print('Finish creating ansers')

    def create_likes(self, count):
        print('Creating likes')
        users = User.objects.all()
        questions = models.Question.objects.all()
        answers = models.Answer.objects.all()
        mas = [0, 1, 1]
        answers = [models.AnswerLike(user=random.choice(users), answer=random.choice(answers), is_true=random.choice(mas)) for i in range (count)]
        print('tut 1')
        questions = [models.QuestionLike(user=random.choice(users), question=random.choice(questions), is_true=random.choice(mas)) for i in range (count)]
        print('tut 2')
        models.AnswerLike.objects.bulk_create(answers, ignore_conflicts=True)
        print('tut 3')
        models.QuestionLike.objects.bulk_create(questions, ignore_conflicts=True)
        print('Finish creating likes')

