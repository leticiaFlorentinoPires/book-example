from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch, call
from django.contrib import auth

class SendLoginEmailViewTest(TestCase):

    @patch('accounts.views.send_mail')
    def test_redirects_to_home_page(self, mock_send_email):
        response = self.client.post(reverse('send_email'), data={'email': 'bob@gmail.com'})
        
        (subject, msg,email_from,email_to), kwargs = mock_send_email.call_args
        
        self.assertEqual(mock_send_email.called, True)
        self.assertEqual(subject,"subject_1")
        self.assertEqual(msg,"message_1")
        self.assertEqual(email_from,"lepirescomp@gmail.com")
        self.assertEqual(email_to, ["bob@gmail.com"])

    @patch('accounts.views.auth')
    def test_login(self, mock_auth):
        self.client.get('/accounts/login?token=abcd123')
        self.assertEqual(mock_auth.authenticate.call_args, call(uid='abcd123'))
        
