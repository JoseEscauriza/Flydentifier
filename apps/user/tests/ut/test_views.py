# basic test class + request generator
from django.test import TestCase, RequestFactory
# for failed authentication test
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse  # for reverse-lookup on url names
from apps.user import views, models


# class TestUserView(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()

#         self.user = models.User.objects.create_user(
#             username='testuser',
#             password="testpassword",
#             first_name="test",
#             last_name="user",
#             email="test@user.com",
#             bio="Test user for... testing.",
#         )

#     def test_profile_redirect_for_unauthorized_user(self):
#         url = reverse("user-dashboard")
#         # call http get method on specified url
#         request = self.factory.get(url)
#         request.user = AnonymousUser()  # Assign anon user to the user of our request

#         response = views.UserDashboard.get(self, request)

#         self.assertEqual(response.status_code, 302)
