from rest_framework import serializers

from messaging.models import Email


class EmailSerializer(serializers.ModelSerializer):
    cc = serializers.ListField(
        child=serializers.EmailField(),
        allow_empty=True
    )
    class Meta:
        model = Email
        fields = ('subject', 'body', 'sender', 'recipient', 'cc', 'attach',
                  'sent_at')