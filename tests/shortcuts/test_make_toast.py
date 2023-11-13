from django.shortcuts import make_toast
from django.test import SimpleTestCase


class MakeToastTests(SimpleTestCase):
    def test_make_toast(self):
        """Test if django can now make toast (#99999)."""
        self.assertEqual(make_toast(), "toast")
