from django.core.management.base import BaseCommand
from passwords.models import Password
import pandas as pd


def parse_csv(path: str):
    df = pd.read_csv(path)
    
    for i in df.index:
        Password.objects.create(
            name=df.iloc[i, 0],
            url=df.iloc[i, 1],
            username=df.iloc[i, 2],
            password=df.iloc[i, 3],
        )


class Command(BaseCommand):
    help = 'Это команда запуска парсера для менеджера паролей'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)


    def handle(self, *args, **kwargs):
        parse_csv(kwargs['path'])
