# from allauth.account.models import EmailAddress
# from django.test import TestCase
# from django.urls import reverse_lazy
# from django.contrib import admin
# from django.contrib.staticfiles import finders

# from home.models import CustomUser


# class Test(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         """
#         run this setup before any test
#         """

#         cls.user = CustomUser.objects.create_user(
#             username="jackie",
#             email="jackdoe@test.com",
#             password="testpassword",
#             is_active=True,
#             is_superuser=True,
#             is_staff=True
#         )

#         EmailAddress.objects.create(
#             user=cls.user, email=cls.user.email, verified=True, primary=True
#         )

#     def test_real_user_can_login(self):
#         """
#         Test if login url works and a user with valid credentials can sign-in
#         """
#         res = self.client.post(
#             reverse_lazy("account_login"),
#             data={"login": self.user.email, "password": "testpassword"},
#         )

#         self.assertEqual(res.status_code, 302)
#         self.assertTrue(res.wsgi_request.user.is_authenticated)

#     def test_fake_user_cannot_login(self):
#         """
#         Test if a user with invalid credentials is unable to sign in
#         """
#         res = self.client.post(
#             reverse_lazy("account_login"),
#             data={"login": "daniel", "password": "password"},
#         )
#         # print(res.content)
#         self.assertFalse(res.wsgi_request.user.is_authenticated)
#         self.assertEqual(res.status_code, 200)

#     def test_signup_page(self):
#         """
#         Check if the signup page opens succesfully
#         """
#         res = self.client.get(reverse_lazy("account_signup"))
#         self.assertEqual(res.status_code, 200)

#     def test_signout_page(self):
#         """
#         Check if the signout page opens succesfully
#         """
#         self.client.post(
#             reverse_lazy("account_login"),
#             data={"login": self.user.email, "password": "testpassword"},
#         )
#         signout_response = self.client.get(reverse_lazy("account_logout"))
#         self.assertEqual(signout_response.status_code, 200)

#     def test_meet_the_ceo__page(self):
#         """
#         Check if meet the ceo page opens succesfully
#         """
#         res = self.client.get(reverse_lazy("home:meet-the-ceo"))
#         self.assertEqual(res.status_code, 200)

#     def test_admin_pages_load_correctly(self):
#         """
#         Checks to ensure no errors when loading model admin page
#         """
#         self.client.force_login(self.user)

#         for model, _ in admin.site._registry.items():
#             meta = model._meta
#             url = f"admin:{meta.app_label}_{meta.model_name}_changelist"
#             res = self.client.get(reverse_lazy(url) + "?q=a")

#             print(f"TESTING {reverse_lazy(url)}")
#             self.assertEqual(res.status_code, 200)

#     def test_password_reset_key_done_page(self):
#         """
#         Check if the signup page opens succesfully
#         """
#         res = self.client.get("/accounts/password/reset/key/done/")
#         self.assertEqual(res.status_code, 200)

#     def test_password_reset_done_page(self):
#         """
#         Check if the password reset page opens succesfully
#         """
#         res = self.client.get(
#             "/accounts/password/reset/done/"
#             )
#         self.assertEqual(res.status_code, 200)

#     def test_logo_presence(self):
#         """
#         Check if the logo displays successfully
#         """
#         logo_response = bool(finders.find('images/logos/logo-xm-dark.png'))
#         favicon_response = bool(finders.find('images/logos/favicon.ico'))

#         self.assertTrue(logo_response)
#         self.assertTrue(favicon_response)
