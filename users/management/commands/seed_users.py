#!/usr/bin/env python3
import random, os
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from django.core.files import File
from django.contrib.admin.utils import flatten
from config.settings import BASE_DIR
from users.models import User


class Command(BaseCommand):

    help = "Эта команда генерирует пользователей в базе данных"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            help="Сколько пользователей создать в базе данных",
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        seeder = Seed.seeder()
        path = os.path.join(BASE_DIR, "uploads/avatars")
        files = os.listdir(
            path,
        )

        seeder.add_entity(
            User,
            number,
            {
                "patronymic": lambda x: seeder.faker.first_name(),
                "is_staff": False,
                "is_superuser": False,
                "avatar": lambda x: f"/avatars/{random.choice(files)}",
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} пользователей создано!"))
