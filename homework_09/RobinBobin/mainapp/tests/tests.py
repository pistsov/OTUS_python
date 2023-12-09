from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from django.utils.translation import gettext_lazy as _


class ProductAddTest(TestCase):
    def test_succ_product_add(self):
        response = self.client.post(
            path="/products/add/",
            data={
                'name': 'cucumber',
                'ccal': 999
            }
        )
        self.assertEqual(302, response.status_code)
