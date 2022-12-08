from rest_framework import serializers
from snippets.models import Snippet, STYLE_CHOICES, LANGUAGE_CHOICES, LEXERS


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']