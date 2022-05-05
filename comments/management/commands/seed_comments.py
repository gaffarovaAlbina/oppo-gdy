import random, os
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from questions.models import Question
from users.models import User
from comments.models import Comment


class Command(BaseCommand):

    help = "Эта команда генерирует комментарии в базе данных"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            help="Сколько комментариев создать в базе данных",
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        seeder = Seed.seeder()
        all_users = User.objects.all()
        all_questions = Question.objects.all()
        seeder.add_entity(
            Comment,
            number,
            {
                "owner": lambda x: random.choice(all_users),
                "question": lambda x: random.choice(all_questions),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} комментариев создано!"))
