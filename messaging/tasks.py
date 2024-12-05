from celery import shared_task


@shared_task
def send_email_async(email_id):
    from django.core.mail import EmailMessage
    from messaging.models import Email
    try:
        email = Email.objects.get(id=email_id)
        subject = email.subject
        message = email.body
        from_email = 'testipeyman@gmail.com'

        email_message = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=[email.recipient],
            cc=email.cc
        )

        email_message.send(fail_silently=False)

        email.status = 'sent'
        email.sent_at = email.created_at
        email.save()

    except Exception as e:
        email.status = 'failed'
        email.error_message = str(e)
        email.save()
