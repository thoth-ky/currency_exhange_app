# Standard Library
import logging

from django.test import Client
from django.test import TestCase

# Third-Party Imports


logging.disable(logging.WARNING)


class CoreBaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls):

        super().setUpClass()
        cls.client = Client()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
