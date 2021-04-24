from unittest import TestCase


class CommonTestCase(TestCase):
    def test_unknown_url(self):
        response = self.client.get('/incorrect/')
        self.assertEqual(response.status_code, 404)
