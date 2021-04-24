from django.contrib.auth.models import User
from django.test import TestCase

from follow.models import Follow


class UserTestCase(TestCase):
    def test_empty_list_users(self):
        response = self.client.get('/v1/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "count": 0,
            "next": None,
            "previous": None,
            "results": []
        })

    def test_list_users_with_users(self):
        User.objects.create(username='Kelly')
        User.objects.create(username='John')
        response = self.client.get('/v1/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "username": "John",
                },
                {
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "username": "Kelly"
                },
            ]
        })
