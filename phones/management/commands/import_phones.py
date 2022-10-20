import csv
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phones = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phones)
            for phone in phones:
                new_phone = Phone.objects.create(
                    id=int(phone[0]), name=phone[1],
                    price=int(phone[3]), image=phone[2],
                    release_date=phone[4],
                    lte_exist=phone[5],
                    slug=slugify(phone[1]),
                )