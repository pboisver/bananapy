from unittest import TestCase

from app import hello_world


class Test(TestCase):
    def test_hello_world(self):
        self.assertEqual('Hello World!', hello_world())
