from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.authentication import PasswordlessAuthenticationBackend
from accounts.models import Token, User

User = get_user_model()

class AuthenticateTest(TestCase):
    
    def test_return_none_if_no_token(self):
        result = PasswordlessAuthenticationBackend().authenticate("test_uuid")
        self.assertIsNone(result)
    
    def test_return_user_if_token_exists_but_no_user(self):
        email = "test@test.com"
        token = Token.objects.create(email=email)
        result_user = PasswordlessAuthenticationBackend().authenticate(token.uid)
        user = User.objects.get(email=token.email)
        
        self.assertEquals(user, result_user)

    def test_return_user_if_token_exists_when_already_has_user(self):
        email = "test2@test.com"
        user = User.objects.create(email=email)
        token = Token.objects.create(email=email)
        result_user = PasswordlessAuthenticationBackend().authenticate(token.uid)
        
        self.assertEquals(user, result_user)

    def test_get_user_exists(self):
        email = "test3@test.com"
        User.objects.create(email="another@test.com")
        user = User.objects.create(email=email)
        result_user = PasswordlessAuthenticationBackend().get_user(email)
        self.assertEquals(user, result_user)
    
    def test_get_user_not_exists(self):
        result_user = PasswordlessAuthenticationBackend().get_user("xyz")
        self.assertIsNone(result_user)

