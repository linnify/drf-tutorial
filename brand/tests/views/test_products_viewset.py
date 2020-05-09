from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.tests.factories import StaffUserFactory


class TestProductsViewSet(APITestCase):
    def setUp(self):
        """Define the test client """
        self.user = StaffUserFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user, token=None)

    @property
    def url(self):
        return f"/products"

    def test_list_all_products(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
