import random, os
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from config.settings import BASE_DIR
import events.models as event_models


class Command(BaseCommand):

    help = "Эта команда генерирует новости в базе данных"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            help="Сколько новостей создать в базе данных",
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        seeder = Seed.seeder()
        seeder.add_entity(
            event_models.Event,
            number,
        )

        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))

        path = os.path.join(BASE_DIR, "uploads/events_photos")
        files = os.listdir(
            path,
        )

        for pk in created_clean:
            event = event_models.Event.objects.get(pk=pk)
            for i in range(1, random.randint(1, 10)):
                event_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"/events_photos/{random.choice(files)}",
                    event=event,
                )

        self.stdout.write(self.style.SUCCESS(f"{number} новостей создано!"))
