import os

from django.conf import settings
from django.core.management import BaseCommand
from django.db import DatabaseError, transaction

from main.models import Registries, Code


class Command(BaseCommand):
    help = 'Command for first required data'
    all = ['regions', 'currencies', 'groups', 'find']

    @transaction.atomic
    def handle(self, *args, **options):
        try:
            print('Commands: ', ', '.join(self.all))
            commands = input('Enter which you would you like to install: ')

            command_list = commands.split(' ')
            if command_list[0] == 'all':
                command_list = self.all

            for command in command_list:
                func = getattr(self, command, self.not_method)
                func(method_name=command)

            self.stdout.write(self.style.SUCCESS(f'Installation is completed successfully'))
        except DatabaseError as e:
            self.stdout.write(self.style.ERROR(f'Please flush the database in order to run install command \n{e}'))

    def not_method(self, method_name):
        self.stdout.write(self.style.ERROR(f'Method with name `{method_name}` does not exist'))

    def test_database(self, **_):
        test_database_list = ['files', 'users', ]
        os.system(f'cd {settings.BASE_DIR}')
        os.system(f'source ../environment')
        os.system(f'source ./.venv/bin/activate')
        os.system(f'python manage.py check')
        for table in test_database_list:
            os.system(f'python manage.py loaddata apps/core/fixtures/{table}')

    def find(self, **_):
        registries = Registries.objects.all()
        for registrie in registries:
            registrie.itt_cd = None
            registrie.save()
