from django.core.mail import EmailMultiAlternatives

def send_feedback_email(subject, text_content, user_email, html_content):
    msg = EmailMultiAlternatives(subject, text_content, 'FancyChamps <verify@fancychamps.com>', [user_email])
    msg.attach_alternative(html_content, "text/html")
    try:
        msg.send(fail_silently=False)
    except Exception as e:
        print(e)

    # send_mail(name,message+" \n "+email,email,['recepients email'],fail_silently=False)

            # current_site = get_current_site(request)
            # subject = 'Welcome to FancyChamps! Confirm Your FancyChamps email.'
            # htmly     = get_template('account_activation_email.html')

            # d = { 'user': user, 'domain':current_site.domain, 'uemail':urlsafe_base64_encode(force_bytes(user.email)), 'uid':urlsafe_base64_encode(force_bytes(user.pk)), 'token': account_activation_token.make_token(user)}

            # # subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
            # text_content = ""
            # html_content = htmly.render(d)
            # msg = EmailMultiAlternatives(subject, text_content, '', [user.email])
            # msg.attach_alternative(html_content, "text/html")
