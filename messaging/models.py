from django.db import models


class CCRecipient(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


    class Meta:
        verbose_name = "CC Recipient"
        verbose_name_plural = "CC Recipients"
        ordering = ['email']


class Email(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed')
    ]

    subject = models.CharField(max_length=32)
    body = models.TextField(blank=True)
    sender = models.EmailField()
    recipient = models.EmailField()
    cc = models.ManyToManyField(CCRecipient, blank=True)
    attach = models.FileField(upload_to='attachments/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    sent_at = models.DateField(null=True, blank=True)
    error_message = models.TextField(blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.subject} - {self.recipient}"

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"


