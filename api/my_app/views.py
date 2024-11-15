from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import MusicianSerializer, BandSerializer
from .models import Musician, Band


@api_view()
def hello_world_view(request: Request) -> Response:
    return Response({'message': 'Hello world!'})


class MusicianViewSet(ModelViewSet):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all().order_by('-pk')


class ListTgUsersView(APIView):
    def get(self, request: Request, format=None):
        tg_users = [musician.user_tg for musician in Musician.objects.all()]
        return Response(tg_users)


class BandViewSet(ModelViewSet):
    serializer_class = BandSerializer
    queryset = Band.objects.all().order_by('-pk')


class ListTgBandsView(APIView):
    def get(self, request: Request, format=None):
        tg_users = [band.user_tg for band in Band.objects.all()]
        return Response(tg_users)


class AllProfileView(APIView):

    def get(self, request: Request, *args, **kwargs):
        response = {}
        mus = Musician.objects.filter(user_tg=self.kwargs['user_tg'])
        band = Band.objects.filter(user_tg=self.kwargs['user_tg'])
        serialized_musician = MusicianSerializer(mus, many=True)
        serialized_band = BandSerializer(band, many=True)
        response.setdefault("Анкета музыканта", serialized_musician.data)
        response.setdefault("Анкета группы", serialized_band.data)
        return Response(response)
