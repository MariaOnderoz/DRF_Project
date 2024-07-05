from rest_framework.serializers import ValidationError

link = "youtube.com"


def validate_youtube(value):
    if link not in value.lower():
        raise ValidationError("Некорректная ссылка")

