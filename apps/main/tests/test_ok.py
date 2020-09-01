from core.rest_framework.tests import BaseTest
from rest_framework import status
from django.urls import reverse


class CalculationOkTest(BaseTest):
    list_url = 'main:calculation-calculation-ok'

    def test_odobrenie(self):
        data = dict(
            type='odobrenie',
            number=200,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

        data = dict(
            type='odobrenie',
            number=200,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

    def test_expansion(self):
        data = dict(
            type='expansion',
            number=200,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

    def test_actualization(self):
        data = dict(
            type='actualization',
            number=200,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)
