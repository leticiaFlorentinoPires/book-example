from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect

# Create your views here.
def send_login_email(request):
    email = request.POST['email']
    send_mail("subject_1", "message_1","lepirescomp@gmail.com",[email])
    return redirect('/')
