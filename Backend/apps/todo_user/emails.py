from django.core.mail import send_mail
import random
from django.conf import settings
from .models import *



def send_otp_via_email(email):
    subject = 'Account Verification Email'
    otp =  random.randint(1000,9999)
    message = f'Your OTP is {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from , recipient_list)


    #save this otp to corresponding user in the database
    user_obj = UserData.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()
