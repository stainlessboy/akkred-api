from __future__ import print_function

from weasyprint import HTML, CSS

from django.conf import settings
from django.template import loader

from main.models import ConfirmReestr
import datetime

class AkkredPDF(object):
    is_choice = {
        True: 'ДА',
        False: 'НЕТ',
    }

    def __init__(self, akkred, request):
        self.request = request
        self.akkred: ConfirmReestr = akkred
        self.content = None
        self.data = dict()
        self.styles = self.get_stylesheets()


    def get_stylesheets(self):
        return [
            CSS(f'{settings.STATIC_ROOT}/pdf/assets/PNG/OZAS-1.png'),

        ]

    def merge_info(self):
        from datetime import datetime as data
        created_date = data.date(data.now())
        self.data.update(
            title_organ=self.akkred.title_organ,
            created_date=created_date
        )

    def generate(self):
        self.merge_info()
        self.content = loader.render_to_string(
            'printable/pdf/index.html', self.data)

    def get_output(self):
        return HTML(
            string=self.content,
            base_url=self.request.build_absolute_uri()
        ).write_pdf(stylesheets=self.styles)
