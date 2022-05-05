from datetime import timedelta
import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
import questions.models as question_models
import users.models as user_models


class Command(BaseCommand):

    help = "Эта команда генерирует вопросы в базе данных"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            help="Сколько вопросов создать в базе данных",
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        seeder.add_entity(
            question_models.Question,
            number,
            {
                "owner": lambda x: random.choice(all_users),
                "answer": lambda x: None,
                "created_answer": lambda x: None,
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} вопросов создано!"))
