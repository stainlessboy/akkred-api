from core.rest_framework.tests import BaseTest
from rest_framework import status
from django.urls import reverse


class CalculationTest(BaseTest):
    list_url = 'main:calculation-calculation'

    def test_accreditation(self):
        data = dict(
            type='accreditation',
            calculation_type='expertise',
            number=200,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

        data = dict(
            type='accreditation',
            calculation_type='site',
            number=200,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

    def test_expansion(self):
        data = dict(
            type='expansion',
            calculation_type='expertise',
            number=200,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

        data = dict(
            type='accreditation',
            calculation_type='site',
            number=200,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

    def test_actualization(self):
        data = dict(
            type='actualization',
            number=200,
            calculation_type='site',
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)
