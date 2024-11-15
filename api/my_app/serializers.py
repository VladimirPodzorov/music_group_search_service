from rest_framework import serializers

from .models import Musician, Band


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = (
            "pk",
            "name",
            "age",
            "musical_instrument",
            "experience",
            "info",
            "avatar",
            "sample",
            "user_tg",
        )


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = (
            "pk",
            "name",
            "musical_genre",
            "who_need",
            "info",
            "sample",
            "user_tg",
        )
