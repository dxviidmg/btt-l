from django.core.mail import send_mail

send_mail('Subject here', 'Here is the message.', 'dxviidmg@gmail.com', ['david@ixulabs.com'], fail_silently=False)