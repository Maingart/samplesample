from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from follow.models import Follow


class FollowTestCase(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create(username="Kevin")
        self.user2 = User.objects.create(username="Tom")
        self.user3 = User.objects.create(username="Jerrie")
        Follow.objects.create(follower=self.user1, follows=self.user2)

    def test_data_is_ready(self):
        self.assertEqual(User.objects.count(), 3)
        self.assertEqual(Follow.objects.count(), 1)

    def test_new_follow_correct(self):
        self.client.force_login(self.user1)
        response = self.client.post(f'/v1/follow/{self.user3.username}/')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Follow.objects.count(), 2)
        self.assertIsNotNone(Follow.objects.filter(
            follower=self.user1, follows=self.user3
        ))

    def test_unfollow_correct(self):
        self.client.force_login(self.user1)
        response = self.client.delete(f'/v1/follow/{self.user2.username}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Follow.objects.count(), 0)

    def test_follow_yourself_failed(self):
        self.client.force_login(self.user1)
        response = self.client.post(f'/v1/follow/{self.user1.username}/')
        self.assertEqual(response.status_code, 400)

    def test_unfollow_not_exists_return_fail(self):
        self.client.force_login(self.user1)
        response = self.client.post(f'/v1/follow/{self.user1.username}/')
        self.assertEqual(response.status_code, 400)

    def test_follow_duplicate_failed(self):
        self.client.force_login(self.user1)
        self.assertEqual(Follow.objects.count(), 0)
        response = self.client.post(f'/v1/follow/{self.user2.username}/')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Follow.objects.count(), 0)
