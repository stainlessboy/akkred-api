from core.rest_framework.tests import BaseTest
from rest_framework import status
from django.urls import reverse


class DocumentsTest(BaseTest):
    list_url = 'main:documents-list'
    list_parent_url = 'main:doc-parent-list'
    detail_url = 'main:documents-detail'

    def test_list(self):
        response = self.client.get(reverse(self.list_url), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)

        print(response.data)


    # def test_list_parent(self):
    #     response = self.client.get(reverse(self.list_parent_url), format='json')
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK,
    #                      response.data)
    #
    #
    #     for  results in response.data['results']:
    #         print(results)