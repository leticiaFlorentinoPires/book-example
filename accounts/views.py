from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import auth

# Create your views here.
def send_login_email(request):
    email = request.POST['email']
    send_mail("subject_1", "message_1","lepirescomp@gmail.com",[email])
    return redirect('/')

def login(request):
    uid = request.GET.get('token')
    import pdb; pdb.set_trace()
    user = auth.authenticate(uid=uid)
    if user is not None:
        auth.login(request,user)
    return redirect('/')
