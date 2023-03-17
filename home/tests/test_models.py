from allauth.account.models import EmailAddress
from django.test import TestCase

from home.models import CustomUser


class Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        run this setup before any test
        """

        cls.user = CustomUser.objects.create_user(
            username="jackie",
            email="jackdoe@test.com",
            password="testpassword",
            is_active=True,
            is_superuser=True,
            is_staff=True
        )

        EmailAddress.objects.create(
            user=cls.user, email=cls.user.email, verified=True, primary=True
        )

    def test_user_is_created(self):
        """
        Test if command creates user
        """
        self.assertEqual(CustomUser.objects.count(), 1)
