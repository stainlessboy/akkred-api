from core.rest_framework.tests import BaseTest
from rest_framework import status
from django.urls import reverse


class CalculationTest(BaseTest):
    list_url = 'main:calculation-calculation-two'

    def test_accreditation(self):
        data = dict(
            type='accreditation',
            calculation_type='expertise',
            numSI=200,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

        data = dict(
            type='accreditation',
            calculation_type='site',
            numSI=200,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

    def test_expansion(self):
        data = dict(
            type='expansion',
            calculation_type='expertise',
            numSI=200,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

        data = dict(
            type='accreditation',
            calculation_type='site',
            numSI=200,
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

    def test_actualization(self):
        data = dict(
            type='actualization',
            numSI=200,
            calculation_type='site',
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

    def test_inspection_control(self):
        data = dict(
            type='inspection_control',
            numSI=200,
            num_test=14001,
            calculation_type='site',
        )
        response = self.client.post(reverse(self.list_url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)
