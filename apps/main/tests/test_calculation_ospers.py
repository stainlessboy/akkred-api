from core.rest_framework.tests import BaseTest
from rest_framework import status
from django.urls import reverse


class CalculationPoiTest(BaseTest):
    list_url = 'main:calculation-calculation-ospers'

    def test_accreditation(self):
        data = dict(
            type='accreditation',
            calculation_type='expertise',
            number=200,
            number2=200,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

        data = dict(
            type='accreditation',
            calculation_type='site',
            number=200,
            number2=200,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

    def test_expansion(self):
        data = dict(
            type='expansion',
            calculation_type='expertise',
            number=200,
            number2=200,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

        data = dict(
            type='accreditation',
            calculation_type='site',
            number=200,
            number2=200,
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

    def test_inspection_control(self):
        data = dict(
            type='inspection_control',
            number2=200,
            number_inspection=14001,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

    def test_inspection_control_fail(self):
        data = dict(
            type='inspection_control',
            number=200,
            number_inspection=14001,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST,
                         response.data)
