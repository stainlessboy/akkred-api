from __future__ import print_function

import datetime
from io import BytesIO
from weasyprint import HTML, CSS

from django.conf import settings
from django.template import loader
from main.models.registries import Registries
from core.utils.attribute import get_attribute


class AkkredPDF(object):
    is_choice = {
        True: 'ДА',
        False: 'НЕТ',
    }

    def __init__(self, akkred, request):
        self.request = request
        self.akkred: Registries = akkred
        self.content = None
        self.data = dict()
        self.styles = self.get_stylesheets()


    def get_stylesheets(self):
        return [
            CSS(f'{settings.STATIC_ROOT}/pdf/assets/PNG/OZAS-1.png'),

        ]

    def merge_info(self):
        self.data.update(
            title=self.akkred.title_yurd_lisa,
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
