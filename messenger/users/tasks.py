from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from celery import shared_task
from .models import MyUser 

#TODO: configure redis and celery settings;move to separate module
@shared_task
def sendMailToNewUser (pk): 
    user = MyUser.objects.get(pk=pk)
    print (f'PK of user during send mail = {user.pk}')
    to = user.email 
    context_data = {'username': user.username}
    subject = 'Добро пожаловать!'
    text_content = f"""
        Dear {to},
        Thanks for registering in my email sender app.
        
        Regards, 
        Maxim 
        """
    html_content = render_to_string('users/welcome_email.html', context=context_data)
    msg = EmailMultiAlternatives (
        subject=subject,
        body=text_content,
        to=[to],
    )
    msg.attach_alternative(html_content, 'text/html')
    try:
        msg.send(fail_silently=False)
        print (f'Mustve sent the email to {to}')
    except Exception as e:
        print(e)
    