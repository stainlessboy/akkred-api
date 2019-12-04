import os

from django.conf import settings
from django.core.management import BaseCommand
from django.db import DatabaseError, transaction

from main.models import Registries


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
        find_list = \
            [{'parent': 69, 'child': 61, 'area': '070344'},
             {'parent': 288, 'child': 282, 'area': '070988'},
             {'parent': 440, 'child': 437, 'area': '071131'},
             {'parent': 501, 'child': 499, 'area': '071172'},
             {'parent': 521, 'child': 20, 'area': '071193'},
             {'parent': 832, 'child': 272, 'area': 'sl0004'},
             {'parent': 834, 'child': 830, 'area': 'sl0001'},
             {'parent': 838, 'child': 441, 'area': 'sl0007'},
             {'parent': 840, 'child': 22, 'area': '071202'}]
        simmilar = []
        registries = Registries.objects.all()
        for registrie in registries:
            res = Registries.objects.filter(area=registrie.area)
            if res.exists():
                sim = res.first()
                if registrie.id != sim.id:
                    simmilar.append(dict(parent=registrie.id, child=sim.id))
                # print(registrie, sim.id)
        print(simmilar)
