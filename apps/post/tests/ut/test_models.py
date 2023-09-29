from django.test import TestCase
from apps.post import models
from apps.user.models import User


class TestPostModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password="testpassword",
            first_name="test",
            last_name="user",
            email="test@user.com",
            bio="Test user for... testing.",
        )

        self.testmodel = models.Post(
            user_id=self.user,
            title="TEST POST",
            body="THIS IS A TEST POST",
        )

    def test_post_print_method(self):
        result = self.testmodel

        self.assertEqual(str(result), "testuser - TEST POST")

    def test_post_username_method(self):
        result = self.testmodel.username()

        self.assertEqual(result, "testuser")


class TestTagModel(TestCase):
    def setUp(self):
        self.testtag = models.Tag(
            name="testtaggy"
        )

    def test_tag_str_method(self):
        result = str(self.testtag)

        self.assertEqual(result, "testtaggy")
